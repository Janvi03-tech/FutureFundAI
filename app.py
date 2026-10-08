import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="FutureFund AI",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SIMPLE PROFESSIONAL CSS
# =========================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Main content width */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1450px;
    }

    /* Main headings */
    h1 {
        color: #172033 !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #172033 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #263449 !important;
        font-weight: 700 !important;
    }

    /* Normal text */
    p {
        color: #526176;
    }

    /* Metric boxes */
    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #e5e9f0;
        border-radius: 16px;
        padding: 18px;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04);
    }

    div[data-testid="stMetricLabel"] {
        color: #64748b !important;
        font-weight: 600 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #172033 !important;
        font-weight: 800 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #172033;
    }

    section[data-testid="stSidebar"] h1 {
        color: white !important;
    }

    section[data-testid="stSidebar"] p {
        color: #cbd5e1 !important;
    }

    section[data-testid="stSidebar"] label {
        color: #e2e8f0 !important;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        border: 1px solid #d8dee9;
    }

    /* Progress bar */
    div[data-testid="stProgressBar"] {
        border-radius: 20px;
    }

</style>
""", unsafe_allow_html=True)

# =========================================================
# SAMPLE DATA
# =========================================================

default_income = 40000
default_expenses = 25000
default_savings = 100000

monthly_surplus = default_income - default_expenses

emergency_target = default_expenses * 6

car_target = 800000
house_target = 4000000
retirement_target = 15000000


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def future_value(monthly_investment, annual_return, years):

    monthly_rate = annual_return / 100 / 12
    months = years * 12

    if monthly_rate == 0:
        return monthly_investment * months

    return monthly_investment * (
        ((1 + monthly_rate) ** months - 1)
        / monthly_rate
    )


def format_rupees(value):
    return f"₹{value:,.0f}"


def financial_health_score(income, expenses, savings):

    score = 0

    if income > expenses:
        score += 40

    if expenses <= income * 0.70:
        score += 20

    if savings >= expenses * 6:
        score += 25
    elif savings >= expenses * 3:
        score += 18
    elif savings >= expenses:
        score += 10

    if income > 0:
        score += 15

    return min(score, 100)


health_score = financial_health_score(
    default_income,
    default_expenses,
    default_savings
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("💰 FutureFund AI")

st.sidebar.caption("SMART FINANCIAL PLANNING")
st.sidebar.caption("AI-powered financial planning")

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👤 My Profile",
        "🎯 Financial Goals",
        "💰 Savings & Investments",
        "🛡️ Insurance",
        "📈 Retirement",
        "🔄 What-If Simulator",
        "🤖 AI Financial Assistant",
        "🗺️ My Financial Roadmap",
        "ℹ️ About FutureFund AI"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "Educational prototype only. "
    "FutureFund AI does not guarantee investment returns "
    "or execute financial transactions."
)

# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------

    st.title("💰 FutureFund AI")

    st.write(
        "Your personal financial planning and future simulation dashboard."
    )

    st.caption(
        "Understand your current position • Plan your goals • Explore possible futures"
    )

    st.divider()

    # -----------------------------------------------------
    # TOP SUMMARY
    # -----------------------------------------------------

    st.subheader("📊 Financial Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Monthly Income",
            value="₹40,000",
            help="Your current monthly income."
        )

    with col2:
        st.metric(
            label="Monthly Expenses",
            value="₹25,000",
            help="Your current monthly expenses."
        )

    with col3:
        st.metric(
            label="Monthly Surplus",
            value="₹15,000",
            help="Income remaining after monthly expenses."
        )

    with col4:
        st.metric(
            label="Current Savings",
            value="₹1,00,000",
            help="Current savings available."
        )

    st.write("")

    # -----------------------------------------------------
    # HEALTH + QUICK SUMMARY
    # -----------------------------------------------------

    left, right = st.columns([1, 1.5])

    with left:

        st.subheader("❤️ Financial Health")

        with st.container(border=True):

            st.metric(
                "Financial Health Score",
                f"{health_score}/100"
            )

            st.progress(
                health_score / 100
            )

            if health_score >= 80:
                st.success(
                    "Your current financial position is healthy."
                )
            elif health_score >= 60:
                st.warning(
                    "Your financial position is reasonable, but there is room to improve."
                )
            else:
                st.error(
                    "Your current financial position needs attention."
                )

    with right:

        st.subheader("💡 AI Financial Insight")

        with st.container(border=True):

            st.markdown("### Your current position")

            st.write(
                "You currently have a positive monthly surplus of "
                "**₹15,000**."
            )

            st.write(
                "You already have **₹1,00,000 in savings**, which provides "
                "a starting point for building your emergency fund."
            )

            st.write(
                "A sensible next step is to strengthen your emergency fund "
                "before increasing long-term investment risk."
            )

    st.write("")
    st.divider()

    # -----------------------------------------------------
    # EMERGENCY FUND
    # -----------------------------------------------------

    st.subheader("🛡️ Emergency Fund")

    emergency_progress = min(
        default_savings / emergency_target,
        1
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Current Emergency Savings",
            "₹1,00,000"
        )

    with col2:

        st.metric(
            "Illustrative Target",
            format_rupees(emergency_target)
        )

    with col3:

        st.metric(
            "Fund Progress",
            f"{emergency_progress * 100:.0f}%"
        )

    st.progress(emergency_progress)

    st.caption(
        "Illustrative target = approximately 6 months of current expenses."
    )

    st.write("")
    st.divider()

    # -----------------------------------------------------
    # GOALS
    # -----------------------------------------------------

    st.subheader("🎯 Financial Goals")

    goal1, goal2, goal3 = st.columns(3)

    with goal1:

        with st.container(border=True):

            st.markdown("### 🚗 Car")

            st.write("Target amount")

            st.markdown("## ₹8,00,000")

            st.progress(0.35)

            st.caption(
                "Illustrative progress: 35%"
            )

    with goal2:

        with st.container(border=True):

            st.markdown("### 🏠 House")

            st.write("Target amount")

            st.markdown("## ₹40,00,000")

            st.progress(0.15)

            st.caption(
                "Illustrative progress: 15%"
            )

    with goal3:

        with st.container(border=True):

            st.markdown("### 🌴 Retirement")

            st.write("Target amount")

            st.markdown("## ₹1,50,00,000")

            st.progress(0.08)

            st.caption(
                "Illustrative progress: 8%"
            )

    st.write("")
    st.divider()

    # -----------------------------------------------------
    # FINANCIAL GROWTH
    # -----------------------------------------------------

    st.subheader("📈 Illustrative Financial Growth")

    st.write(
        "If ₹15,000 is invested every month, this chart shows an "
        "illustrative projection using a 10% annual return assumption."
    )

    years = np.arange(1, 11)

    projected_values = [
        future_value(
            monthly_surplus,
            10,
            int(year)
        )
        for year in years
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=years,
            y=projected_values,
            mode="lines+markers",
            name="Illustrative Future Value",
            line=dict(width=4),
            marker=dict(size=8)
        )
    )

    fig.update_layout(
        height=420,
        xaxis_title="Years",
        yaxis_title="Illustrative Value (₹)",
        paper_bgcolor="white",
        plot_bgcolor="white",
        hovermode="x unified",
        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.caption(
        "This projection is illustrative only. Actual investment returns "
        "may be higher or lower."
    )

    st.divider()

    # -----------------------------------------------------
    # WHAT SHOULD YOU DO NEXT?
    # -----------------------------------------------------

    st.subheader("🚀 Recommended Next Steps")

    next1, next2, next3 = st.columns(3)

    with next1:

        with st.container(border=True):

            st.markdown("### 1. 🛡️ Strengthen Emergency Fund")

            st.write(
                "Work toward maintaining a financial buffer for "
                "unexpected expenses."
            )

    with next2:

        with st.container(border=True):

            st.markdown("### 2. 🎯 Define Your Goals")

            st.write(
                "Set target amounts and timelines for your major "
                "financial goals."
            )

    with next3:

        with st.container(border=True):

            st.markdown("### 3. 🔄 Explore What-If Scenarios")

            st.write(
                "Compare how changes in investment amount, return "
                "assumptions and time can affect future values."
            )

    st.divider()

    st.caption(
        "⚠️ FutureFund AI is an educational decision-support prototype, "
        "not professional financial advice."
    )


# =========================================================
# MY PROFILE
# =========================================================

elif page == "👤 My Profile":

    st.title("👤 My Financial Profile")

    st.write(
        "Enter basic financial information to create your personalized plan."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Personal Information")

        name = st.text_input(
            "Name",
            "Jagan"
        )

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=22
        )

        retirement_age = st.number_input(
            "Target Retirement Age",
            min_value=40,
            max_value=80,
            value=60
        )

    with col2:

        st.subheader("Financial Information")

        income = st.number_input(
            "Monthly Income (₹)",
            min_value=0,
            value=40000,
            step=1000
        )

        expenses = st.number_input(
            "Monthly Expenses (₹)",
            min_value=0,
            value=25000,
            step=1000
        )

        savings = st.number_input(
            "Current Savings (₹)",
            min_value=0,
            value=100000,
            step=5000
        )

    st.divider()

    risk = st.selectbox(
        "Risk Preference",
        [
            "Conservative",
            "Moderate",
            "Aggressive"
        ]
    )

    if st.button("💾 Save Profile"):

        surplus = income - expenses

        st.success(
            "Your financial profile has been processed."
        )

        st.metric(
            "Monthly Surplus",
            format_rupees(surplus)
        )


# =========================================================
# FINANCIAL GOALS
# =========================================================

elif page == "🎯 Financial Goals":

    st.title("🎯 Financial Goal Planner")

    st.write(
        "Turn your financial goals into measurable targets."
    )

    st.divider()

    goal = st.selectbox(
        "Select a financial goal",
        [
            "Emergency Fund",
            "Car",
            "House",
            "Education",
            "Marriage",
            "Travel",
            "Retirement",
            "Custom Goal"
        ]
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        target_amount = st.number_input(
            "Target Amount (₹)",
            min_value=1000,
            value=800000,
            step=10000
        )

    with col2:

        current_amount = st.number_input(
            "Current Amount (₹)",
            min_value=0,
            value=100000,
            step=5000
        )

    with col3:

        years = st.number_input(
            "Time Available (Years)",
            min_value=1,
            max_value=50,
            value=5
        )

    remaining = max(
        target_amount - current_amount,
        0
    )

    monthly_required = remaining / (years * 12)

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Goal",
            goal
        )

    with col2:
        st.metric(
            "Remaining Amount",
            format_rupees(remaining)
        )

    with col3:
        st.metric(
            "Simple Monthly Requirement",
            format_rupees(monthly_required)
        )

    st.progress(
        min(current_amount / target_amount, 1)
    )

    st.info(
        "This is a simplified planning calculation. "
        "Inflation, taxes and actual investment returns are not included."
    )


# =========================================================
# SAVINGS & INVESTMENTS
# =========================================================

elif page == "💰 Savings & Investments":

    st.title("💰 Savings & Investments")

    st.write(
        "Compare common savings and investment options for educational planning."
    )

    st.divider()

    data = {
        "Option": [
            "Savings Account",
            "Fixed Deposit (FD)",
            "Recurring Deposit (RD)",
            "Mutual Fund / SIP",
            "Stocks"
        ],
        "Purpose": [
            "Liquidity",
            "Stable savings",
            "Regular savings",
            "Long-term growth",
            "Higher-risk growth"
        ],
        "Risk Level": [
            "Low",
            "Low",
            "Low",
            "Moderate",
            "High"
        ]
    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("📊 SIP Projection")

    col1, col2, col3 = st.columns(3)

    with col1:

        monthly = st.number_input(
            "Monthly Investment (₹)",
            min_value=500,
            value=5000,
            step=500
        )

    with col2:

        annual_return = st.number_input(
            "Illustrative Annual Return (%)",
            min_value=0.0,
            max_value=30.0,
            value=10.0,
            step=0.5
        )

    with col3:

        investment_years = st.number_input(
            "Investment Period (Years)",
            min_value=1,
            max_value=50,
            value=10
        )

    projected = future_value(
        monthly,
        annual_return,
        investment_years
    )

    st.metric(
        "Illustrative Future Value",
        format_rupees(projected)
    )

    st.warning(
        "This is a mathematical illustration and is not a guarantee of returns."
    )


# =========================================================
# INSURANCE
# =========================================================

elif page == "🛡️ Insurance":

    st.title("🛡️ Insurance Planning")

    st.write(
        "Understand major insurance categories that can form part "
        "of a financial plan."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        with st.container(border=True):

            st.subheader("🏥 Health Insurance")

            st.write(
                "Helps manage financial risks related to medical expenses."
            )

    with col2:

        with st.container(border=True):

            st.subheader("❤️ Term Insurance")

            st.write(
                "Can provide financial protection to dependents "
                "during the policy term."
            )

    with col3:

        with st.container(border=True):

            st.subheader("🚑 Accident Insurance")

            st.write(
                "Can provide protection against certain accident-related risks."
            )

    st.divider()

    st.warning(
        "FutureFund AI does not recommend specific insurance companies "
        "or policies. Always review coverage, exclusions, premiums and "
        "policy terms carefully."
    )


# =========================================================
# RETIREMENT
# =========================================================

elif page == "📈 Retirement":

    st.title("📈 Retirement Planner")

    st.write(
        "Estimate a possible retirement corpus using simplified assumptions."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        current_age = st.number_input(
            "Current Age",
            min_value=18,
            max_value=70,
            value=22
        )

        retirement_age = st.number_input(
            "Retirement Age",
            min_value=40,
            max_value=80,
            value=60
        )

        monthly_investment = st.number_input(
            "Monthly Investment (₹)",
            min_value=500,
            value=10000,
            step=500
        )

    with col2:

        expected_return = st.number_input(
            "Illustrative Annual Return (%)",
            min_value=0.0,
            max_value=30.0,
            value=10.0,
            step=0.5
        )

        inflation = st.number_input(
            "Illustrative Inflation (%)",
            min_value=0.0,
            max_value=15.0,
            value=6.0,
            step=0.5
        )

    years_to_retirement = max(
        retirement_age - current_age,
        0
    )

    corpus = future_value(
        monthly_investment,
        expected_return,
        years_to_retirement
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Illustrative Retirement Corpus",
            format_rupees(corpus)
        )

    with col2:

        st.metric(
            "Years to Retirement",
            years_to_retirement
        )

    st.warning(
        "Retirement projections are highly sensitive to inflation, "
        "returns, expenses and life expectancy."
    )


# =========================================================
# WHAT-IF SIMULATOR
# =========================================================

elif page == "🔄 What-If Simulator":

    st.title("🔄 What-If Financial Simulator")

    st.write(
        "Explore how changing your assumptions can affect an illustrative future value."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        investment = st.slider(
            "Monthly Investment (₹)",
            1000,
            50000,
            10000,
            1000
        )

    with col2:

        years = st.slider(
            "Investment Period",
            1,
            30,
            10
        )

    with col3:

        return_rate = st.slider(
            "Illustrative Return (%)",
            1.0,
            20.0,
            10.0,
            0.5
        )

    projected_value = future_value(
        investment,
        return_rate,
        years
    )

    total_contribution = investment * years * 12

    growth = projected_value - total_contribution

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Contributions",
            format_rupees(total_contribution)
        )

    with col2:

        st.metric(
            "Illustrative Future Value",
            format_rupees(projected_value)
        )

    with col3:

        st.metric(
            "Illustrative Growth",
            format_rupees(max(growth, 0))
        )

    st.divider()

    st.subheader("📊 Scenario Comparison")

    scenarios = {
        "Lower": 6,
        "Moderate": 10,
        "Higher": 14
    }

    scenario_values = []

    for scenario, rate in scenarios.items():

        value = future_value(
            investment,
            rate,
            years
        )

        scenario_values.append({
            "Scenario": scenario,
            "Illustrative Return": f"{rate}%",
            "Future Value": format_rupees(value)
        })

    st.dataframe(
        pd.DataFrame(scenario_values),
        use_container_width=True,
        hide_index=True
    )

    st.warning(
        "These scenarios are hypothetical assumptions, not predictions."
    )


# =========================================================
# AI FINANCIAL ASSISTANT
# =========================================================

elif page == "🤖 AI Financial Assistant":

    st.title("🤖 AI Financial Assistant")

    st.write(
        "Ask questions about savings, financial goals, investments "
        "and long-term financial planning."
    )

    st.divider()

    st.info(
        "The current version contains an AI assistant prototype. "
        "An LLM API can be connected in the next development stage."
    )

    question = st.text_area(
        "Your Question",
        placeholder=(
            "Example: I earn ₹40,000 per month. "
            "How should I plan for a car in 5 years?"
        ),
        height=140
    )

    if st.button("🤖 Ask FutureFund AI"):

        if question.strip():

            st.success(
                "Question received."
            )

            st.subheader("AI Planning Approach")

            st.write(
                "FutureFund AI would analyze your question together with "
                "your income, expenses, savings, goals, time horizon and "
                "risk preference."
            )

            st.write(
                "The system would then use the financial calculation engine "
                "for numerical results and the LLM for explanation and "
                "personalization."
            )

        else:

            st.warning(
                "Please enter a question first."
            )


# =========================================================
# FINANCIAL ROADMAP
# =========================================================

elif page == "🗺️ My Financial Roadmap":

    st.title("🗺️ My Financial Roadmap")

    st.write(
        "A simple step-by-step roadmap for improving your long-term financial position."
    )

    st.divider()

    roadmap = [
        (
            "1️⃣",
            "Understand Your Cash Flow",
            "Track your income, expenses and monthly surplus."
        ),
        (
            "2️⃣",
            "Build an Emergency Fund",
            "Create a financial buffer for unexpected expenses."
        ),
        (
            "3️⃣",
            "Define Your Goals",
            "Set measurable financial targets and timelines."
        ),
        (
            "4️⃣",
            "Choose Suitable Options",
            "Compare savings and investment options according to "
            "your time horizon and risk preference."
        ),
        (
            "5️⃣",
            "Plan for Retirement",
            "Start long-term retirement planning early."
        ),
        (
            "6️⃣",
            "Review Your Plan",
            "Update the plan when your income, expenses or goals change."
        )
    ]

    for number, title, description in roadmap:

        with st.container(border=True):

            st.subheader(f"{number} {title}")

            st.write(description)

        st.write("")


# =========================================================
# ABOUT
# =========================================================

elif page == "ℹ️ About FutureFund AI":

    st.title("ℹ️ About FutureFund AI")

    st.write(
        "FutureFund AI is an LLM-powered personalized financial planning "
        "and long-term financial simulation system."
    )

    st.divider()

    st.subheader("🎯 Main Idea")

    st.write(
        "The system answers a simple question:"
    )

    st.info(
        "“If I make this financial decision today, what could my "
        "financial future look like?”"
    )

    st.subheader("🧩 Main Components")

    components = pd.DataFrame({
        "Component": [
            "User Profile",
            "Financial Health Check",
            "Emergency Fund",
            "Goal Planner",
            "Financial Engine",
            "Scenario Engine",
            "LLM",
            "Safety Layer",
            "Financial Roadmap"
        ],
        "Purpose": [
            "Stores basic financial information",
            "Understands current financial position",
            "Checks financial emergency buffer",
            "Converts goals into measurable targets",
            "Performs deterministic calculations",
            "Explores possible future scenarios",
            "Understands and explains user questions",
            "Reduces misleading or overconfident responses",
            "Creates an organized planning sequence"
        ]
    })

    st.dataframe(
        components,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("🔬 Research Gap")

    st.write(
        "Traditional financial calculators usually focus on individual "
        "calculations, while conversational AI can explain concepts but "
        "should not be trusted for deterministic financial mathematics."
    )

    st.write(
        "FutureFund AI combines conversational interaction with a "
        "deterministic financial calculation engine and scenario simulation."
    )

    st.divider()

    st.subheader("⚠️ Disclaimer")

    st.warning(
        "FutureFund AI is an educational and decision-support prototype. "
        "It does not provide guaranteed investment returns, execute "
        "financial transactions or replace qualified financial professionals."
    )