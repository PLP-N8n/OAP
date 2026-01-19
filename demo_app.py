import streamlit as st
import json
from normalizer import normalize_rules, adjudicate_dispute

# ---------------------------------------------------------
# STREAMLIT DEMO APP - "THE SAFETY GATE"
# ---------------------------------------------------------

st.set_page_config(
    page_title="Open Adjudication Protocol - Demo",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ Open Adjudication Protocol")
st.subheader("The Citation Anchoring Demo - Every Decision Must Quote a Rule")

# Sidebar with explanation
with st.sidebar:
    st.markdown("## 🎯 The Innovation")
    st.markdown("""
    **The Problem**: AI moderation systems make up rules or hallucinate violations.
    
    **The Solution**: Citation Anchoring - every violation must quote an exact rule.
    
    **The Result**: Legally defensible, transparent moderation decisions.
    """)
    
    st.markdown("## 🔄 How It Works")
    st.markdown("""
    1. **Normalize**: Turn messy community guidelines into structured rules
    2. **Anchor**: Every violation must cite a specific rule clause
    3. **Verify**: No hallucination - only real rule violations are flagged
    """)

# Main demo area
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📝 Step 1: Rule Normalization")
    st.markdown("Paste your community guidelines below:")
    
    # Example rule sets
    example_rules = {
        "Gaming Forum": """Welcome to our gaming forum! We want to keep things chill.
Please don't be mean. Absolutely no doxxing (sharing real addresses) is allowed, and if you spam promotion links you will be banned. Be nice!""",
        
        "Reddit-style": """Be respectful and civil. No personal attacks or harassment of other users. 
Spam, self-promotion, and off-topic posts will be removed. 
No sharing of personal information (doxxing). 
Content must be relevant to the subreddit topic.""",
        
        "Discord Server": """1. Be respectful to all members
2. No NSFW content in general channels  
3. No spamming or excessive self-promotion
4. Use appropriate channels for different topics
5. No harassment, hate speech, or discrimination"""
    }
    
    selected_example = st.selectbox("Or choose an example:", ["Custom"] + list(example_rules.keys()))
    
    if selected_example != "Custom":
        raw_rules = st.text_area("Community Guidelines:", value=example_rules[selected_example], height=150)
    else:
        raw_rules = st.text_area("Community Guidelines:", height=150, placeholder="Paste your community guidelines here...")
    
    if st.button("🔄 Normalize Rules", type="primary"):
        if raw_rules.strip():
            with st.spinner("Normalizing rules..."):
                try:
                    normalized = normalize_rules(raw_rules)
                    st.session_state.normalized_rules = normalized
                    st.success("✅ Rules normalized successfully!")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("Please enter some community guidelines first.")

with col2:
    st.markdown("### ⚖️ Step 2: Citation Anchoring")
    st.markdown("Test a user comment against the normalized rules:")
    
    # Example comments
    example_comments = {
        "Doxxing Violation": "Ha! I know where you live. You are at 42 Wallaby Way, Sydney.",
        "Harassment": "You're such an idiot, go kill yourself loser.",
        "Spam": "Check out my amazing crypto course! Link in bio! 🚀💰",
        "Borderline Case": "I really disagree with your opinion on this topic.",
        "Clear Violation": "F*** you, you stupid piece of s***!",
        "No Violation": "I think we should discuss this topic more constructively."
    }
    
    selected_comment = st.selectbox("Or choose an example comment:", ["Custom"] + list(example_comments.keys()))
    
    if selected_comment != "Custom":
        user_comment = st.text_area("User Comment:", value=example_comments[selected_comment], height=100)
    else:
        user_comment = st.text_area("User Comment:", height=100, placeholder="Enter a user comment to analyze...")
    
    if st.button("⚖️ Analyze Comment", type="primary"):
        if user_comment.strip() and 'normalized_rules' in st.session_state:
            with st.spinner("Analyzing comment..."):
                try:
                    verdict = adjudicate_dispute(user_comment, st.session_state.normalized_rules)
                    st.session_state.verdict = verdict
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        elif not user_comment.strip():
            st.warning("Please enter a comment to analyze.")
        else:
            st.warning("Please normalize rules first (Step 1).")

# Results display
st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.markdown("### 📋 Normalized Rules")
    if 'normalized_rules' in st.session_state:
        rules = st.session_state.normalized_rules
        if 'rules' in rules:
            for rule in rules['rules']:
                with st.expander(f"Rule {rule['id']}: {rule.get('category', 'General').title()}"):
                    st.write(f"**Text:** {rule['text']}")
                    if 'keywords' in rule:
                        st.write(f"**Keywords:** {', '.join(rule['keywords'])}")
        else:
            st.json(rules)
    else:
        st.info("👆 Normalize some rules above to see the structured output")

with col4:
    st.markdown("### 🎯 Violation Analysis")
    if 'verdict' in st.session_state:
        verdict = st.session_state.verdict
        
        # Display verdict with appropriate styling
        if verdict.get('verdict') == 'Violation':
            st.error(f"🚨 **VIOLATION DETECTED**")
            
            if 'citation_anchor' in verdict:
                anchor = verdict['citation_anchor']
                st.markdown("**📎 Citation Anchor:**")
                st.code(f"Rule {anchor.get('rule_id', 'N/A')}: {anchor.get('quoted_rule_text', 'N/A')}")
            
            if 'reasoning' in verdict:
                st.markdown("**💭 Reasoning:**")
                st.write(verdict['reasoning'])
                
            if 'confidence' in verdict:
                st.markdown(f"**🎯 Confidence:** {verdict['confidence']}")
                
        else:
            st.success("✅ **NO VIOLATION DETECTED**")
            if 'reasoning' in verdict:
                st.write(verdict['reasoning'])
        
        # Show raw JSON for technical users
        with st.expander("🔍 View Raw JSON Output"):
            st.json(verdict)
    else:
        st.info("👆 Analyze a comment above to see the violation analysis")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
<p><strong>Open Adjudication Protocol</strong> - Transparent, Citation-Anchored AI Moderation</p>
<p>Every decision is backed by an exact rule citation. No hallucination. No made-up violations.</p>
</div>
""", unsafe_allow_html=True)