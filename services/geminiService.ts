import { GoogleGenAI, Type } from "@google/genai";
import { AdjudicationResult } from '../types';

export const adjudicateContent = async (rulebook: string, content: string): Promise<AdjudicationResult> => {
  if (!process.env.API_KEY) {
    throw new Error("API Key is missing. Please ensure process.env.API_KEY is available.");
  }

  const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });

  const systemInstruction = `
    You are the Open Adjudication Protocol (OAP) Engine. 
    Your ONLY purpose is to determine if a piece of content violates the provided Rulebook.
    
    PRINCIPLE OF CITATION ANCHORING:
    1. You CANNOT find a violation unless you can quote the EXACT sentence from the rulebook that was broken.
    2. If the user's content is offensive but does not violate a specific written rule, you MUST return "NO_VIOLATION".
    3. You must not hallucinate rules.
    
    Output JSON format only.
  `;

  const prompt = `
    RULEBOOK:
    ${rulebook}

    CONTENT TO ADJUDICATE:
    ${content}
  `;

  try {
    const response = await ai.models.generateContent({
      model: 'gemini-3-flash-preview',
      contents: prompt,
      config: {
        systemInstruction: systemInstruction,
        responseMimeType: "application/json",
        responseSchema: {
          type: Type.OBJECT,
          properties: {
            verdict: {
              type: Type.STRING,
              enum: ['VIOLATION', 'NO_VIOLATION'],
              description: 'The final decision on the content.',
            },
            citation: {
              type: Type.STRING,
              nullable: true,
              description: 'The exact quote from the Rulebook that was violated. Null if no violation.',
            },
            reasoning: {
              type: Type.STRING,
              description: 'A brief explanation linking the citation to the content.',
            },
          },
          required: ['verdict', 'reasoning'],
        },
      },
    });

    if (response.text) {
      return JSON.parse(response.text) as AdjudicationResult;
    }
    
    throw new Error("Empty response from OAP Engine");

  } catch (error) {
    console.error("Adjudication failed:", error);
    throw error;
  }
};