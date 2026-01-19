import React, { useEffect, useState } from 'react';
import { ArrowLeft, FileText } from 'lucide-react';

const WHITEPAPER_BLOCKS = [
  `The Architecture of Digital Justice: A Comprehensive Analysis of the Open Adjudication Protocol (OAP)`,
  `1. Introduction: The Crisis of Legitimacy in Digital Governance`,
  `The digital ecosystem currently stands at a precipice. For two decades, the governance of online spaces has been defined by a paradigm of opaque enforcement, characterized by "benevolent dictatorships" where platforms wield absolute, often inscrutable authority over user speech and conduct. This era, driven by the necessity of managing exponential scale, prioritized speed and volume over nuance and explanation. Trust and Safety (T&S) teams, operating as the judiciary of the internet, have historically relied on blunt instruments - mass bans, automated takedowns, and keyword filters - to maintain order. However, as the digital commons has matured into the primary arena for global discourse, commerce, and civic life, the limitations of this enforcement-first model have become critically apparent.1`,
  `The Open Adjudication Protocol (OAP), as detailed in its Product Requirements Document (PRD), represents a distinct and necessary pivot in the evolution of platform governance. It signals a shift from enforcement to adjudication, and from opacity to radical visibility. OAP is defined not merely as a moderation tool, but as "B2B Trust & Safety Infrastructure" designed to provide a "transparent, AI-assisted reasoning layer" for online disputes.1 This distinction is profound. While existing market solutions focus on the detection of harmful content or the workflow of human moderators, OAP focuses on the legibility of reasoning - the ability to explain, in structured and legally defensible terms, why a decision was made.`,
  `The emergence of OAP is not an isolated product launch but a response to three converging systemic crises identified in the research: the operational unsustainability of human moderation, the psychological erosion of user trust due to perceived unfairness, and a tidal wave of global regulation demanding "due process" rights for digital citizens.`,
  `1.1 The Operational and Economic Crisis`,
  `The first driver of this shift is the economic and operational limit of the current model. The PRD explicitly identifies "Operational Cost" as a systemic challenge, noting that human moderation is "expensive, slow, inconsistent, and psychologically taxing".1 As platforms scale, the linear addition of human reviewers yields diminishing returns. The psychological toll on moderators - often exposed to the worst of human behavior - leads to high turnover and cognitive fatigue, which in turn fuels inconsistency in decision-making. This phenomenon, known as "moderator drift," renders platform rules unpredictable.`,
  `Conversely, the traditional automation used to alleviate this burden - keyword blocking, hash matching, and early machine learning classifiers - has historically lacked the semantic nuance to explain its actions. A classifier might output a probability score indicating "95% likelihood of toxicity," but it cannot articulate the reasoning required to satisfy a confused user or a skeptical regulator.2 The gap between the scalability of AI and the explainability of humans has created a "legibility gap" that OAP aims to bridge.1`,
  `1.2 The Trust Deficit and Procedural Justice`,
  `The second crisis is relational. Users are increasingly disengaging from platforms where moderation feels arbitrary. The PRD cites "Perceived Unfairness" as a primary cause of user churn and escalation.1 When a user receives a generic notification citing a violation of "Community Guidelines" without specific evidence or rationale, the interaction is perceived as authoritarian rather than corrective.`,
  `Research into "procedural justice" theory - which OAP implicitly operationalizes - suggests that people care as much about the fairness of the process as they do about the outcome.3 If users believe their voice was heard, the process was neutral, and the authority acted with trustworthy motives, they are more likely to accept even negative outcomes.5 By failing to provide this procedural transparency, current platforms inadvertently incentivize recidivism and conflict. OAP's mandate to "illuminate disputes" rather than issue verdicts is a direct architectural response to this psychological reality.1`,
  `1.3 The Regulatory Imperative`,
  `The third, and perhaps most immediate, driver is the regulatory landscape, dominated by the European Union's Digital Services Act (DSA). The DSA has fundamentally altered the compliance requirements for online platforms. Specifically, Article 17 mandates that providers must provide a "clear and specific statement of reasons" to any user affected by a content restriction.6 This statement must include the facts relied upon, the specific legal or contractual ground for the decision, and information on the use of automated means.7`,
  `The scale of this requirement is staggering. Data from the EU Transparency Database indicates that in a single six-month period, just 116 platforms generated over 9.4 billion statements of reasons.8 It is physically impossible for human teams to draft this volume of legalistic explanations. Consequently, platforms face a binary choice: deploy "template" responses that risk regulatory non-compliance for being too vague, or adopt advanced AI solutions capable of generating specific, case-by-case reasoning at scale. OAP positions itself as the infrastructure for the latter.1`,
  `2. The Regulatory Landscape: The Digital Services Act and the Transparency Mandate`,
  `To fully understand the market gap OAP addresses, one must analyze the specific requirements of the Digital Services Act (DSA), which serves as the de facto global standard for content moderation transparency. The DSA moves beyond the era of "self-regulation" into a regime of "regulated transparency," where the internal logic of moderation is subject to external audit.`,
  `2.1 Article 17: The "Statement of Reasons" (SoR)`,
  `Article 17 is the fulcrum of the DSA's consumer protection framework. It requires that platforms explain their decisions to the affected user. The requirements for this explanation are rigorous. Snippets from the DSA text and legal analyses clarify that a Statement of Reasons must contain:`,
  `- Information on the restriction: What specifically was removed or demoted? 6
- The facts and circumstances: A description of the content and the context in which it was posted.9
- The legal or contractual ground: A specific citation of the law or Terms of Service (ToS) clause that was violated.7
- Use of automated means: A disclosure of whether AI was used for detection or decision-making.9`,
  `The OAP PRD aligns its core features directly with these requirements. The "Dispute Analysis Engine" is designed to output a structured JSON object containing a "Neutral summary of each party's claims" (facts and circumstances) and "Rule citations with exact quoted text" (contractual ground).1 This design suggests that OAP is not just a general-purpose dispute tool, but a purpose-built compliance engine for Article 17. By automating the drafting of these fields, OAP transforms a massive administrative burden into a programmatic API call.`,
  `2.2 The Transparency Database and API Integration`,
  `The DSA does not just require that explanations be sent to users; it requires that they be centralized. Article 24(5) mandates that Very Large Online Platforms (VLOPs) submit their Statements of Reasons to a publicly accessible "DSA Transparency Database" managed by the European Commission.8 This database allows researchers, regulators, and the public to scrutinize moderation trends.`,
  `Crucially, the Commission has released an API for this database, allowing for automated submission.10 The OAP architecture appears designed to interface seamlessly with this infrastructure. The fields generated by OAP - restriction type, rule citation, summary - map directly to the schema required by the Transparency Database API.11 This interoperability is a significant strategic advantage. For a platform using OAP, the workflow would be seamless:`,
  `- Ingestion: Dispute data is sent to OAP.
- Analysis: OAP generates the Statement of Reasons (SoR).
- Delivery: The SoR is displayed to the user (Article 17 compliance).
- Reporting: The SoR is pushed via API to the EU Transparency Database (Article 24 compliance).`,
  `2.3 Beyond the DSA: Global Ripples`,
  `While the DSA is the immediate catalyst, the demand for "explainability" is becoming a global norm. In the United States, state-level regulations like the Colorado AI Act and various "automated decision-making" statutes are beginning to require similar disclosures regarding how AI impacts consumer rights.13 Furthermore, the rise of "AI Ethics" boards and internal compliance teams 15 creates a market for tools that can demonstrate "algorithmic accountability." OAP's "Norm Source Declaration" and "Human-in-Control" principles 1 provide the necessary audit trails to satisfy these emerging global frameworks.`,
  `3. The Philosophy of OAP: Doctrine-Driven Infrastructure`,
  `Unlike many software products that function as neutral tools configured entirely by the user, OAP is "Doctrine-Driven." It imposes a specific philosophical and ethical framework on the adjudication process. The PRD states that these principles are "immutable and override all customer configuration".1 This approach effectively positions OAP as a "Constitution as a Service," enforcing a baseline of procedural integrity regardless of the specific platform using it.`,
  `3.1 Radical Visibility`,
  `The first pillar of the OAP Doctrine is Radical Visibility, mandating that "all reasoning is visible to involved parties by default".1 This principle challenges the prevailing "security through obscurity" mindset in Trust and Safety, where moderation rules are often kept vague to prevent bad actors from gaming the system.`,
  `OAP argues that obscurity breeds distrust. Drawing on sociological concepts of "radical visibility" found in organizational management and political science, the protocol posits that open information flows are essential for collaboration and trust.16 In the context of a dispute, if a user cannot see the logic used to judge them, they cannot learn from the interaction, nor can they effectively appeal.`,
  `The doctrine permits exceptions only for "safety or legal reasons," such as protecting the identity of a reporter in a harassment case. However, OAP introduces a meta-layer of transparency: "Any restriction must itself be disclosed in-system".1 This ensures that even when information is redacted, the fact of redaction is transparent, preventing the "silent suppression" that characterizes authoritarian systems.`,
  `3.2 The Whiteboard Mandate`,
  `The Whiteboard Mandate constrains the system to "illuminate disputes; never issue verdicts".1 This is a critical safety and liability feature. OAP explicitly refuses to be the judge. Instead, it acts as the clerk, preparing the file and summarizing the arguments for the human moderator or the platform's distinct policy engine.`,
  `This separation of analysis (the whiteboard) from judgment (the verdict) addresses the risk of "AI Overreach".1 It aligns with the concept of "augmented justice," where technology supports but does not usurp human moral authority.18 By outputting a "resolution space" (possible paths forward) rather than a binary decision, OAP preserves human agency and mitigating the legal risks associated with fully automated decision-making. If an error is made in the final verdict, the platform can argue that the AI was merely advisory - a crucial distinction for liability under frameworks like Section 230 in the US or the liability exemptions in the EU.`,
  `3.3 Epistemic Humility`,
  `The most intellectually ambitious pillar of the OAP Doctrine is Epistemic Humility. The system must "explicitly state uncertainty and missing context".1 In the current landscape of Generative AI, where Large Language Models (LLMs) are notorious for their "confident ignorance" or "fluent falsehoods" 19, this doctrine is a necessary corrective.`,
  `Epistemic humility is defined in the literature as the recognition that uncertainty is a fundamental aspect of knowledge.20 An epistemically humble system does not pretend to be omniscient. It distinguishes between what it knows (data present in the transcript) and what it infers (intent, context).`,
  `Technical Implementation: If OAP analyzes a comment that could be interpreted as either sarcasm or abuse, but lacks the tonal context to decide, the doctrine requires it to flag this as an "Area of Ambiguity".1`,
  `Trust Dynamics: Research in healthcare and AI ethics suggests that systems which acknowledge their limitations are viewed as more trustworthy and less likely to cause "epistemic injustice" - the harm done when a person's testimony is unfairly dismissed.21 By formalizing "I don't know" as a valid and necessary system output, OAP builds a foundation for long-term trust that "hallucinating" systems cannot match.`,
  `3.4 Norm-Agnosticism and Source Declaration`,
  `Finally, OAP is "norm-agnostic but procedurally fixed".1 It does not supply the values; it supplies the process. The platform (the customer) must supply the "Community Rules." OAP then rigorously applies those specific rules to the dispute. This "Norm Source Declaration" 1 protects OAP from accusations of bias. It is not an "AI Censor" imposing Silicon Valley values on the world; it is a "Procedural Engine" helping a gaming community in Korea or a marketplace in Brazil apply their own local norms consistently.`,
  `4. Procedural Justice in the Algorithmic Age`,
  `OAP's design is deeply rooted in the social science of Procedural Justice. While the PRD uses the term "fairness," the mechanisms it describes map directly to the four pillars of procedural justice identified by researchers like Tom Tyler: Voice, Neutrality, Respect, and Trustworthiness.4`,
  `4.1 The Psychology of Fairness`,
  `Research confirms that in online governance, user compliance is driven more by the perception of fair treatment than by the fear of punishment.5`,
  `- Voice: Users need to feel their side of the story was heard. OAP's "Neutral summary of each party's claims" 1 provides visible proof that the system has "read" and understood the user's input.
- Neutrality: Decisions must be based on rules, not bias. OAP's "Citation Anchoring" (discussed in Section 6) ensures that every point is tethered to a pre-existing rule, demonstrating neutrality.
- Respect: The interaction must be dignified. By providing a "structured, explainable analysis" rather than a silent ban, OAP treats the user as a rational agent capable of understanding the rules.`,
  `4.2 Restoring "Epistemic Trust"`,
  `The internet suffers from a crisis of "epistemic trust" - we no longer trust that the information we see or the decisions made about us are grounded in reality.23 AI often exacerbates this by generating "synthetic" content that blurs truth and fiction. OAP attempts to rebuild this trust by making the "process of knowing" visible.`,
  `The Dialectic of Knowing: By exposing the "Identified points of agreement and disagreement" 1, OAP forces a dialectical process. It shows the user: "Here is what you said, here is what the rule says, and here is where they conflict." This transparency transforms the moderation event from a punitive strike into a pedagogical moment, potentially reducing recidivism.24`,
  `4.3 Automating Due Process`,
  `Historically, "due process" was a luxury only affordable in courts of law. OAP attempts to "industrialize" due process. By using AI to generate the artifacts of justice (summaries, rule citations, reasoning) at the speed of software, it makes high-quality adjudication accessible for low-stakes online disputes. This democratization of justice is critical for the "long tail" of online conflict - the millions of minor disputes that currently fester unresolved because human intervention is too costly.3`,
  `5. Technical Architecture: The Dispute Analysis Engine`,
  `At the heart of OAP lies the Dispute Analysis Engine, the API-driven component responsible for processing disputes. Its design reflects a careful balance between the generative power of LLMs and the constraints necessary for safety.`,
  `5.1 Input Vector: Context and Rules`,
  `The engine accepts a tri-partite input:`,
  `- Conversation transcript: The raw data of the dispute.
- Platform-supplied rules: The normative framework (ToS, guidelines).
- Moderator context: Optional metadata or notes from human reviewers.1`,
  `This structure ensures that the AI is not "hallucinating" norms from its general training data (e.g., "what does the internet generally think is rude?") but is instead "grounded" in the specific legal contract between the platform and the user.`,
  `5.2 Structured Output Schema`,
  `The engine does not output a free-form essay. It generates a strictly defined JSON object.1 This structured output is vital for integration with downstream systems (like the DSA Transparency Database). Key fields include:`,
  `- Neutral summary: A non-evaluative synthesis of claims.
- Rule citations: Exact text extracts from the provided rules.
- Ambiguity flags: Specific indicators of missing information.
- Resolution space: A set of logical next steps.`,
  `This schema serves as a "forcing function" for the AI. By requiring specific fields like "Rule Citations," the system forces the underlying model to perform a retrieval task rather than just a creative writing task.`,
  `5.3 The Resolution Space vs. The Verdict`,
  `The concept of the "Resolution Space" is technically distinct from a "Verdict." A verdict is binary (Ban/No Ban). A resolution space is topological. It might identify:`,
  `- Path A: User apologizes (Restorative Justice).
- Path B: Content is hidden but account remains (Proportional Action).
- Path C: User updates the post to comply with Rule 4 (Correction).`,
  `This nuance allows platforms to move beyond the "Death Penalty" model of moderation (account bans) toward more restorative interactions. It aligns with the "Whiteboard Mandate" by presenting options without executing them.`,
  `6. The Safety Architecture: Citation Anchoring and Hallucination Mitigation`,
  `The single greatest technical risk to OAP is AI Hallucination. In a legal compliance context, a "hallucinated" rule citation (e.g., citing "Section 5.2" when only "Section 5.1" exists) is catastrophic. It exposes the platform to regulatory fines and lawsuits. To counter this, OAP implements a mechanism called Citation Anchoring.`,
  `6.1 The Challenge of "Verifiable Citation" in LLMs`,
  `Research indicates that standard LLMs struggle significantly with accurate citation. Studies show hallucination rates for citations can range from 25% to 90% in generative tasks, and models frequently invent "fluent" but non-existent sources.25 Even Retrieval-Augmented Generation (RAG) systems, which access external data, can have hallucination rates of 17-33% if not strictly constrained.27`,
  `The problem is "over-generalization": models are optimized for linguistic plausibility, not factual verification.29 A model might confidently state, "This violates the harassment policy," because that sounds like a reasonable sentence, even if the specific harassment policy provided does not cover the behavior in question.`,
  `6.2 The OAP Solution: A Hard Safety Gate`,
  `OAP addresses this with a brute-force constraint. The PRD defines Citation Anchoring as a "hard safety gate".1`,
  `- Exact match requirement: Every evaluative statement must cite an exact rule clause. The system is forbidden from using inferred or paraphrased rules.
- The refusal mechanism: If no citation exists, the system must "explicitly state the absence" and "escalate for human review." It must refuse to proceed rather than guess.1`,
  `This "Refusal" capability is cutting-edge in AI safety. Recent research into "selective refusal" shows that the ability of a model to say "I don't know" or "I cannot answer based on provided context" is the defining characteristic of safe deployment.30 By mandating refusal when grounding is absent, OAP prioritizes precision (avoiding false positives) over recall (catching every violation). In a legal context, this is the correct trade-off: it is better to miss a violation than to punish a user based on a fabricated rule.`,
  `6.3 Technical Implementation of Anchoring`,
  `While the PRD is high-level, the implementation likely involves a "Verify-and-Cite" loop similar to "Self-Healing" architectures described in recent literature.26`,
  `Generation: The model proposes a reasoning.
Verification: A secondary process checks if the cited text exists verbatim in the rule set.
Correction: If the check fails, the generation is discarded, and the system defaults to the "Ambiguity/Refusal" state.`,
  `This aligns with findings that "strict citation verification" with overlap checking can achieve near 100% precision in detecting hallucinations.27`,
  `7. Competitive Landscape and Market Positioning`,
  `OAP enters a rapidly evolving Trust & Safety market. To understand its potential, we must map it against the existing incumbents: the Detectors, the Workflow Managers, and the Compliance Reporters.`,
  `7.1 The Detectors: ActiveFence and WebPurify`,
  `ActiveFence and WebPurify are the giants of detection. ActiveFence uses deep intelligence and AI to identify "bad" content across audio, video, and text.32 Its strength is "Safety by Design" and proactive threat intelligence - finding the terrorist cell or the CSAM ring before they act.33`,
  `OAP Distinction: ActiveFence answers the question "Is this bad?" OAP answers the question "Why is this bad?" ActiveFence is the police officer making the arrest; OAP is the court clerk writing the brief. While ActiveFence offers "Red Teaming" and "Guardrails" 35, its primary focus is identifying risk, not explaining it to the end-user.`,
  `Integration: OAP is complementary. An ActiveFence signal (e.g., "Risk Score: High") could be the input for OAP, which then generates the human-readable explanation for the user.`,
  `7.2 The Compliance Managers: Checkstep and Tremau`,
  `Checkstep and Tremau focus on the regulatory workflow.`,
  `Checkstep: Offers a "DSA Plugin" that automates Transparency Reports and Statements of Reasons.36 It positions itself as an "all-in-one" compliance solution.`,
  `Tremau: Positions itself as the "operating system" for T&S, centralizing data and routing tasks.37 It also offers SoR generation.38`,
  `OAP Distinction: These competitors approach SoR generation as a reporting task - filling out a form. OAP approaches it as a reasoning task. Current compliance tools often rely on static templates (mapping a "Hate Speech" tag to a generic "Article 12" citation). OAP's "Dispute Analysis Engine" performs a granular, semantic analysis of the specific conversation. OAP creates a bespoke explanation for this specific dispute, whereas competitors often automate the delivery of generic explanations. OAP competes on the quality and defensibility of the explanation.`,
  `7.3 The Operating Systems: Cinder`,
  `Cinder provides the infrastructure for T&S teams - the dashboard, the data model, the investigation graph.39 It is the "desk" the moderator sits at.`,
  `OAP Distinction: OAP is a feature or integration for Cinder, not a replacement. Cinder manages the case; OAP powers the "Write Decision" button within Cinder's interface.`,
  `7.4 Strategic Positioning: The Logic Layer`,
  `OAP carves out a unique niche as the Logic Layer.`,
  `- Layer 1: Detection (ActiveFence) - Finds the needle in the haystack.
- Layer 2: Workflow (Cinder/Tremau) - Routes the needle to a human.
- Layer 3: Logic/Reasoning (OAP) - Explains why the needle is sharp and violates the rules.
- Layer 4: Reporting (Checkstep/Tremau) - Tells the EU about the needle.`,
  `OAP's specific focus on "doctrine-driven" reasoning allows it to serve as a neutral "middleware" for justice, distinct from the enforcement tools.`,
  `Table 1: Competitive Landscape Analysis`,
  `8. Economic and Operational Impact`,
  `Beyond compliance, OAP offers a compelling economic argument grounded in the reduction of "Failure Demand."`,
  `8.1 Reducing Appeal Volumes (Failure Demand)`,
  `"Failure demand" is demand caused by a failure to do something right the first time. In T&S, a user appeal is often a sign of failure demand - the user appeals because they did not understand the initial decision. The PRD targets "Reduction in user appeals" as a key success metric.1`,
  `Mechanism: By providing a high-quality, evidence-based explanation upfront (via OAP), the platform preempts the user's confusion. If the user clearly sees exactly which rule they broke and exactly which text violated it, they are statistically less likely to appeal.5 This directly reduces the operational load on human appeal queues.`,
  `8.2 The Economics of "Human-in-the-Loop"`,
  `Human moderation is expensive. OAP's "Tier 2 - Review Dashboard" 1 enables a "Cyborg" workflow. Instead of a human writing a decision from scratch (taking 5-10 minutes), the human reviews the OAP-generated analysis (taking 30-60 seconds).`,
  `Efficiency Gain: This moves the human from "Author" to "Editor," potentially increasing moderator throughput by 5-10x while maintaining the quality assurance of human oversight. This directly addresses the "Operational Cost" challenge cited in the PRD.1`,
  `8.3 Mitigating User Churn`,
  `The "Perceived Unfairness" driver 1 is an economic bleed. A banned user is a lost customer. A user who feels treated unfairly but is not banned may still reduce their engagement or become toxic (recidivism). By applying procedural justice, OAP aims to retain users even during conflict. The "Resolution Space" offers paths for redemption (e.g., "edit your post") rather than just exclusion, preserving the user's lifetime value (LTV) to the platform.`,
  `9. Implementation and Integration Strategies`,
  `OAP is designed as an "API-first" infrastructure 1, implying a high degree of modularity.`,
  `9.1 Product Tiers and Delivery`,
  `The PRD outlines three tiers 1:`,
  `- Tier 1 (Utility API): Pure JSON-in/JSON-out. Targeted at platforms with their own custom interfaces (e.g., a gaming company's in-game dispute system).
- Tier 2 (Review Dashboard): A web interface for human review. Targeted at mid-sized platforms without custom T&S tooling.
- Tier 3 (Analytics & Audit): Consistency metrics and trend analysis.`,
  `This tiering strategy allows OAP to penetrate the market at different levels - as a raw engine for tech-forward companies (Tier 1) and as a complete solution for operationally constrained teams (Tier 2).`,
  `9.2 Integration with Regulatory Pipes`,
  `The most critical integration is with the DSA Transparency Database. As detailed in Section 2, the OAP output schema is practically a mirror of the API schema required by the EU Commission.`,
  `Strategy: OAP should offer "One-Click Compliance." "Use OAP to resolve the dispute, and we will automatically format and batch-upload the Statement of Reasons to the EU Database." This feature alone justifies the cost for any VLOP struggling with Article 24 obligations.`,
  `10. Future Horizons: From Tool to Standard`,
  `The long-term vision of OAP is to become a "reference standard".1 This ambition extends beyond software into the realm of digital institution building.`,
  `10.1 The TCP/IP of Justice`,
  `Just as TCP/IP standardized how data packets move, OAP aims to standardize how conflict is processed. Currently, every platform reinvents the wheel of moderation. OAP proposes a shared language: a standard JSON format for a dispute.`,
  `Implication: If OAP becomes a standard, we could see "Portable Reputation" or "Cross-Platform Safety." A rigorous analysis of a user's behavior on Platform A could be intelligibly read by Platform B, not just as a "ban flag" but as a nuanced history of conduct.`,
  `10.2 Risks and Challenges`,
  `- Bureaucratization: There is a risk that OAP creates a "bureaucracy of bots," where users are drowned in technical jargon. The "Epistemic Humility" doctrine must actively fight against the tendency of legalistic systems to become cold and inaccessible.
- The fluency trap: Even with citation anchoring, the risk of "fluent falsehoods" remains. If the platform's own rules are vague or contradictory, OAP will struggle to anchor its reasoning. The system is only as good as the rules it is given.
- Adoption friction: Platforms are protective of their moderation data. Convincing them to pipe this sensitive data through a third-party API (OAP) requires an immense degree of trust and security assurance.`,
  `10.3 Conclusion: The Necessity of Explanation`,
  `The Open Adjudication Protocol arrives at a moment of historical necessity. The era of "move fast and break things" is over; the era of "move fast and explain things" has begun. The convergence of strict regulations (DSA), operational exhaustion, and the crisis of user trust demands a new architecture.`,
  `OAP's genius lies in its refusal to be a judge. By focusing strictly on the explanation - governed by the rigid doctrines of Radical Visibility, the Whiteboard Mandate, and Epistemic Humility - it offers a path to "Industrialized Justice." It leverages the power of AI not to enforce silence, but to articulate the rules of the road, transforming the chaotic noise of online conflict into a legible, navigable, and ultimately more human system. In doing so, it creates the infrastructure for a digital society that is not just policed, but governed.`,
  `Works cited`,
  `Open Adjudication Protocol (oap) - Product Requirements Document.docx`,
  `Proceedings of the Fourth Workshop on NLP for Positive Impact (NLP4PI) - ACL Anthology, accessed on January 19, 2026, https://aclanthology.org/anthology-files/pdf/nlp4pi/2025.nlp4pi-1.pdf`,
  `Online Dispute Resolution | RSI, accessed on January 19, 2026, https://www.aboutrsi.org/special-topics/online-dispute-resolution`,
  `Procedural Justice in Online Deliberation: Theoretical Explanations and Empirical Findings, accessed on January 19, 2026, https://delibdemjournal.org/article/id/968/`,
  `View of Procedural Justice and Self Governance on Twitter | Journal of Online Trust and Safety, accessed on January 19, 2026, https://tsjournal.org/index.php/jots/article/view/38/27`,
  `Article 17, the Digital Services Act (DSA), accessed on January 19, 2026, https://www.eu-digital-services-act.com/Digital_Services_Act_Article_17.html`,
  `Additional Explanation For Statement Attributes - DSA Transparency Database, accessed on January 19, 2026, https://transparency.dsa.ec.europa.eu/page/additional-explanation-for-statement-attributes`,
  `The EU Digital Services Act: Ready to meet reporting obligations? | IAPP, accessed on January 19, 2026, https://iapp.org/news/a/the-eu-digital-services-act-ready-to-meet-reporting-obligations`,
  `The Digital Services Act: Practical Implications for Online Services and Platforms - Latham & Watkins LLP, accessed on January 19, 2026, https://www.lw.com/admin/upload/SiteAttachments/Digital-Services-Act-Practical-Implications-for-Online-Services-and-Platforms.pdf`,
  `API and Schema - DSA Transparency Database - European Union, accessed on January 19, 2026, https://transparency.dsa.ec.europa.eu/page/api-documentation`,
  `DSA Transparency Database : Questions and Answers | Shaping Europe's digital future, accessed on January 19, 2026, https://digital-strategy.ec.europa.eu/en/faqs/dsa-transparency-database-questions-and-answers`,
  `API and Schema - DSA Transparency Database - European Union, accessed on January 19, 2026, https://transparency.dsa.ec.europa.eu/page/api-documentation?lang=en`,
  `[FPF Legislation] Policy Brief: The Colorado AI Act, accessed on January 19, 2026, https://leg.colorado.gov/sites/default/files/images/fpf_legislation_policy_brief_the_colorado_ai_act_final.pdf`,
  `Final Statement of Reasons - California Privacy Protection Agency, accessed on January 19, 2026, https://cppa.ca.gov/regulations/pdf/ccpa_updates_cyber_risk_admt_fsor_and_uid.pdf`,
  `Institutional AI: The Crucial Nexus of Democracy, Civil Virtue, and Ethical AI Governance, accessed on January 19, 2026, https://dr-arsanjani.medium.com/institutional-ai-the-crucial-nexus-of-democracy-civil-virtue-and-ethical-ai-governance-c8731d754735`,
  `Transparency in Organizing - Research@CBS, accessed on January 19, 2026, https://research-api.cbs.dk/ws/portalfiles/portal/58846592/Oana_Albu.pdf`,
  `General Stanley McChrystal: Team of Teams - AgileLeanHouse, accessed on January 19, 2026, https://agileleanhouse.com/en/general-stanley-mcchrystal-team-of-teams.html`,
  `Rethinking Mediation and Arbitration in the Age of Artificial Intelligence: A systematic review | Salud, Ciencia y Tecnologia, accessed on January 19, 2026, https://sct.ageditor.ar/index.php/sct/article/download/2316/2886/10380`,
  `Why Epistemic Humility is the Survival Skill of 2026 - Chris Hood, accessed on January 19, 2026, https://chrishood.com/why-epistemic-humility-is-the-survival-skill-of-2026/`,
  `The Transition from Omniscient AI to Epistemically Honest AI | by Carlos E. Perez - Medium, accessed on January 19, 2026, https://intuitmachine.medium.com/the-transition-from-omniscient-ai-to-epistemically-honest-ai-971309f69b1a`,
  `The need for epistemic humility in AI-assisted pain assessment - PubMed - NIH, accessed on January 19, 2026, https://pubmed.ncbi.nlm.nih.gov/40087254/`,
  `The need for epistemic humility in AI-assisted pain assessment - PMC - NIH, accessed on January 19, 2026, https://pmc.ncbi.nlm.nih.gov/articles/PMC12103351/`,
  `Rebuilding Epistemic Trust in an AI-Mediated Internet - The Decision Lab, accessed on January 19, 2026, https://thedecisionlab.com/big-problems/rebuilding-epistemic-trust-in-an-ai-mediated-internet`,
  `Report: Online Platforms Can Stem Problem Content With a Principle from Criminal Justice, accessed on January 19, 2026, https://law.yale.edu/yls-today/news/report-online-platforms-can-stem-problem-content-principle-criminal-justice`,
  `Review of Reference Generation Methods in Large Language Models - ResearchGate, accessed on January 19, 2026, https://www.researchgate.net/publication/390214708_Review_of_Reference_Generation_Methods_in_Large_Language_Models`,
  `A Self-Healing Architecture for Mitigating Bibliographic Hallucinations in LLM-Generated Academic Texts - ResearchGate, accessed on January 19, 2026, https://www.researchgate.net/publication/398465134_A_Self-Healing_Architecture_for_Mitigating_Bibliographic_Hallucinations_in_LLM-Generated_Academic_Texts`,
  `Citation-Grounded Code Comprehension: Preventing LLM Hallucination Through Hybrid Retrieval and Graph-Augmented Context - arXiv, accessed on January 19, 2026, https://arxiv.org/html/2512.12117v1`,
  `HalluGraph: Auditable Hallucination Detection for Legal RAG Systems via Knowledge Graph Alignment - arXiv, accessed on January 19, 2026, https://arxiv.org/html/2512.01659v1`,
  `Citation Hallucinations - Emergent Mind, accessed on January 19, 2026, https://www.emergentmind.com/topics/citation-hallucinations`,
  `RefusalBench: Generative Evaluation of Selective Refusal in Grounded Language Models - arXiv, accessed on January 19, 2026, https://arxiv.org/html/2510.10390v1`,
  `RefusalBench: Generative Evaluation of Selective Refusal in Grounded Language Models, accessed on January 19, 2026, https://openreview.net/forum?id=EZR72ArmSS&referrer=%5Bthe%20profile%20of%20Aashiq%20Muhamed1%5D(%2Fprofile%3Fid%3D~Aashiq_Muhamed1)`,
  `8 ActiveFence Alternatives - Competitor Features and Pricing Review - GetStream.io, accessed on January 19, 2026, https://getstream.io/blog/activefence-competitors/`,
  `Be Prepared for an AI Crackdown from U.S. State Attorneys General - ActiveFence, accessed on January 19, 2026, https://www.activefence.com/blog/ai-crackdown-state-attorneys-general/`,
  `ActiveFence: Trust Your AI, accessed on January 19, 2026, https://www.activefence.com/`,
  `ActiveFence AI Security Benchmark Report Summary, accessed on January 19, 2026, https://www.activefence.com/blog/activefence-ai-security-benchmark/`,
  `The AI Content Moderation Platform - Checkstep, accessed on January 19, 2026, https://www.checkstep.com/our-platform`,
  `T&S Platform - Content Moderation Platform for Online Safety | Tremau, accessed on January 19, 2026, https://tremau.com/platform/`,
  `Achieving digital platform - public transparency in Australia, accessed on January 19, 2026, https://au.reset.tech/Digital-platform-public-transparency.pdf`,
  `Trust and safety startup Cinder launches from stealth mode with $14M in funding, accessed on January 19, 2026, https://siliconangle.com/2022/12/08/trust-safety-startup-cinder-launches-stealth-mode-14m-funding/`,
];

const blocks = WHITEPAPER_BLOCKS;
const title = blocks[0];
const worksCitedIndex = blocks.findIndex((block) => /^Works cited$/i.test(block));
const bodyBlocks = worksCitedIndex === -1 ? blocks.slice(1) : blocks.slice(1, worksCitedIndex);
const citations = worksCitedIndex === -1 ? [] : blocks.slice(worksCitedIndex + 1);

const isSectionHeading = (block: string) => /^\d+\.\s/.test(block);
const isSubsectionHeading = (block: string) => /^\d+\.\d+\s/.test(block);
const isTableCaption = (block: string) => /^Table\s+\d+:/i.test(block);
const slugify = (value: string) =>
  value
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');

const tocItems = bodyBlocks
  .filter((block) => isSectionHeading(block) || isSubsectionHeading(block))
  .map((block) => ({
    id: slugify(block),
    text: block,
    level: isSubsectionHeading(block) ? 2 : 1,
  }));

if (citations.length > 0) {
  tocItems.push({ id: 'works-cited', text: 'Works cited', level: 1 });
}

const renderBlock = (block: string, index: number) => {
  if (isSubsectionHeading(block)) {
    return (
      <h3
        key={index}
        id={slugify(block)}
        className="text-xl md:text-2xl font-semibold text-white font-display mt-10"
      >
        {block}
      </h3>
    );
  }

  if (isSectionHeading(block)) {
    return (
      <h2
        key={index}
        id={slugify(block)}
        className="text-2xl md:text-3xl font-semibold text-white font-display mt-12"
      >
        {block}
      </h2>
    );
  }

  if (isTableCaption(block)) {
    return (
      <p key={index} className="text-sm text-slate-400 italic">
        {block}
      </p>
    );
  }

  const lines = block.split('\n').map((line) => line.trim()).filter(Boolean);
  if (lines.length > 1 && lines.every((line) => line.startsWith('- '))) {
    return (
      <ul key={index} className="list-disc list-inside space-y-2 text-slate-200 leading-relaxed">
        {lines.map((line, lineIndex) => (
          <li key={lineIndex}>{line.replace(/^- /, '')}</li>
        ))}
      </ul>
    );
  }

  if (lines.length > 1) {
    return (
      <div key={index} className="space-y-2 text-slate-200 leading-relaxed">
        {lines.map((line, lineIndex) => (
          <p key={lineIndex}>{line}</p>
        ))}
      </div>
    );
  }

  return (
    <p key={index} className="text-slate-200 leading-relaxed">
      {block}
    </p>
  );
};

export const Whitepaper: React.FC = () => {
  const [activeId, setActiveId] = useState<string | null>(tocItems[0]?.id ?? null);

  useEffect(() => {
    if (!tocItems.length) {
      return;
    }

    const elements = tocItems
      .map((item) => document.getElementById(item.id))
      .filter((element): element is HTMLElement => Boolean(element));

    if (!elements.length) {
      return;
    }

    setActiveId(elements[0].id);

    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries.filter((entry) => entry.isIntersecting);
        if (!visible.length) {
          return;
        }
        visible.sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        const target = visible[0].target as HTMLElement;
        setActiveId(target.id);
      },
      {
        rootMargin: '-20% 0px -70% 0px',
        threshold: [0.1, 0.5, 1],
      }
    );

    elements.forEach((element) => observer.observe(element));

    return () => observer.disconnect();
  }, []);

  const renderTocLinks = () => (
    <div className="mt-4 grid gap-2 text-sm text-slate-200">
      {tocItems.map((item) => {
        const isActive = item.id === activeId;
        const baseTone = item.level === 2 ? 'pl-4 text-slate-400' : 'text-slate-200';
        return (
          <a
            key={item.id}
            href={`#${item.id}`}
            aria-current={isActive ? 'true' : undefined}
            className={`transition-colors hover:text-teal-200 ${baseTone} ${
              isActive ? 'text-teal-200 font-semibold' : ''
            }`}
          >
            {item.text}
          </a>
        );
      })}
    </div>
  );

  return (
    <main className="min-h-screen text-white">
      <div className="border-b border-white/10 bg-ink-900/80 backdrop-blur-xl sticky top-0 z-40">
        <div className="container mx-auto px-6 h-16 flex items-center justify-between">
          <div className="flex items-center gap-3 font-display font-semibold">
            <div className="w-8 h-8 rounded-md bg-gradient-to-br from-teal-400 via-sky-400 to-amber-400 shadow-lg shadow-teal-500/30"></div>
            <span className="text-lg">Open Adjudication Protocol</span>
          </div>
          <a href="/" className="flex items-center gap-2 text-sm font-semibold text-slate-300 hover:text-white">
            <ArrowLeft className="w-4 h-4" />
            Back to home
          </a>
        </div>
      </div>

      <section className="py-16 md:py-20">
        <div className="container mx-auto px-6">
          <div className="max-w-4xl mx-auto">
            <div className="mb-12">
              <div className="flex items-center gap-3 text-xs uppercase tracking-[0.4em] text-teal-300 font-mono">
                <FileText className="w-4 h-4" />
                Whitepaper
              </div>
              <h1 className="font-display text-3xl md:text-5xl font-semibold text-white mt-4">
                {title}
              </h1>
              <p className="text-slate-400 mt-4 max-w-2xl leading-relaxed">
                Complete text from Whitepaper_oap.docx, formatted for clear reading.
              </p>
            </div>

            <div className="grid gap-10 lg:grid-cols-[1fr_280px]">
              <div>
                {tocItems.length > 0 && (
                  <div className="mb-12 rounded-2xl border border-white/10 bg-ink-900/60 px-6 py-5 lg:hidden">
                    <div className="text-xs uppercase tracking-[0.3em] text-slate-400 font-mono">
                      Table of Contents
                    </div>
                    {renderTocLinks()}
                  </div>
                )}

                <article className="space-y-6">
                  {bodyBlocks.map((block, index) => renderBlock(block, index))}
                </article>

                {citations.length > 0 && (
                  <div className="mt-14">
                    <h2
                      id="works-cited"
                      className="text-2xl md:text-3xl font-semibold text-white font-display"
                    >
                      Works cited
                    </h2>
                    <ul className="mt-4 space-y-3 text-sm text-slate-300 leading-relaxed">
                      {citations.map((citation, index) => (
                        <li key={index}>{citation}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>

              {tocItems.length > 0 && (
                <aside className="hidden lg:block">
                  <div className="sticky top-24 max-h-[calc(100vh-7rem)] overflow-y-auto rounded-2xl border border-white/10 bg-ink-900/60 px-6 py-5">
                    <div className="text-xs uppercase tracking-[0.3em] text-slate-400 font-mono">
                      Table of Contents
                    </div>
                    {renderTocLinks()}
                  </div>
                </aside>
              )}
            </div>
          </div>
        </div>
      </section>
    </main>
  );
};
