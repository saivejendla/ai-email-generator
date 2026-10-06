import streamlit as st

from src.email_generator import generate_email
from src.prompt_builder import build_email_prompt
from src.rewrite_prompt import build_rewrite_prompt


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="AI Email Generator",
    page_icon="✦",
    layout="wide",
)


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(91, 80, 255, 0.13),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(0, 191, 255, 0.08),
                transparent 30%
            ),
            #0b0f19;
    }

    /* Main page width */
    .block-container {
        max-width: 1350px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Gemini badge */
    .ai-badge {
        display: inline-block;
        padding: 6px 13px;
        border-radius: 20px;

        background: rgba(124, 92, 255, 0.12);

        border: 1px solid
            rgba(124, 92, 255, 0.35);

        color: #b9a9ff;

        font-size: 13px;
        font-weight: 600;

        margin-bottom: 14px;
    }

    /* Main title */
    .hero-title {
        font-size: 48px;
        font-weight: 800;
        line-height: 1.05;

        margin-bottom: 10px;

        background: linear-gradient(
            90deg,
            #ffffff,
            #c4b5fd,
            #7dd3fc
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Subtitle */
    .hero-text {
        color: #9ca3af;
        font-size: 17px;

        max-width: 720px;

        margin-bottom: 24px;
    }

    /* Panel heading */
    .panel-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 3px;
    }

    /* Panel description */
    .panel-description {
        color: #8b93a7;
        font-size: 13px;
        margin-bottom: 18px;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        height: 48px;

        border-radius: 10px;
        border: none;

        font-weight: 700;

        background: linear-gradient(
            90deg,
            #6d5dfc,
            #4f8cff
        );

        color: white;
    }

    .stButton > button:hover {
        border: none;
        color: white;

        box-shadow:
            0 0 20px
            rgba(109, 93, 252, 0.35);
    }

    /* Inputs */
    .stTextInput input,
    .stTextArea textarea {
        border-radius: 10px;
    }

    /* Radio buttons */
    div[role="radiogroup"] {
        gap: 15px;
    }

    /* Hide Streamlit footer */
    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ==========================================================
# SESSION STATE
# ==========================================================

if "generated_email" not in st.session_state:
    st.session_state.generated_email = ""


if "current_mode" not in st.session_state:
    st.session_state.current_mode = "✦ Generate Email"


# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    '<div class="ai-badge">✦ POWERED BY GEMINI</div>',
    unsafe_allow_html=True,
)


st.markdown(
    '<div class="hero-title">AI Email Generator</div>',
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="hero-text">
        Generate polished emails from a few ideas or transform
        an existing email into something clearer, stronger and
        more professional.
    </div>
    """,
    unsafe_allow_html=True,
)


# ==========================================================
# MODE SELECTOR
# ==========================================================

mode = st.radio(
    "Choose Mode",
    [
        "✦ Generate Email",
        "✎ Rewrite Email",
    ],
    horizontal=True,
    label_visibility="collapsed",
)


# Clear old output when switching modes
if mode != st.session_state.current_mode:

    st.session_state.generated_email = ""
    st.session_state.current_mode = mode


st.divider()


# ==========================================================
# TWO-COLUMN WORKSPACE
# ==========================================================

left_column, right_column = st.columns(
    [1, 1.15],
    gap="large",
)


# ==========================================================
# LEFT COLUMN
# ==========================================================

with left_column:

    # ======================================================
    # GENERATE EMAIL MODE
    # ======================================================

    if mode == "✦ Generate Email":

        st.markdown(
            '<div class="panel-title">Compose</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="panel-description">
                Tell AI what kind of email you want to create.
            </div>
            """,
            unsafe_allow_html=True,
        )


        # --------------------------------------------------
        # EMAIL TYPE
        # --------------------------------------------------

        email_type = st.selectbox(
            "What are you writing?",
            [
                "Job Application",
                "Follow-up",
                "Thank You",
                "Meeting Request",
                "Leave Request",
                "Client Email",
                "Networking",
                "Custom",
            ],
        )


        # --------------------------------------------------
        # PURPOSE
        # --------------------------------------------------

        if email_type == "Custom":

            purpose = st.text_input(
                "Email Purpose",
                placeholder=(
                    "Example: Request project "
                    "deadline extension"
                ),
            )

        else:

            purpose = email_type


        # --------------------------------------------------
        # RECIPIENT
        # --------------------------------------------------

        recipient = st.text_input(
            "Who is it for?",
            placeholder=(
                "Example: Hiring Manager, "
                "Professor, Client"
            ),
        )


        # --------------------------------------------------
        # CONTEXT
        # --------------------------------------------------

        context = st.text_area(
            "Context",
            placeholder=(
                "Briefly explain the situation...\n\n"
                "Example: I interviewed yesterday "
                "for an AI Engineer position and "
                "want to follow up."
            ),
            height=130,
        )


        # --------------------------------------------------
        # KEY POINTS
        # --------------------------------------------------

        key_points = st.text_area(
            "Key Points",
            placeholder=(
                "What should the email mention?\n\n"
                "Example:\n"
                "- Thank them for their time\n"
                "- Express continued interest\n"
                "- Available for further discussion"
            ),
            height=140,
        )


        # --------------------------------------------------
        # TONE AND LENGTH
        # --------------------------------------------------

        tone_column, length_column = st.columns(2)


        with tone_column:

            tone = st.selectbox(
                "Tone",
                [
                    "Professional",
                    "Friendly",
                    "Formal",
                    "Polite",
                    "Confident",
                    "Warm",
                    "Concise",
                ],
            )


        with length_column:

            length = st.selectbox(
                "Length",
                [
                    "Short",
                    "Medium",
                    "Detailed",
                ],
            )


        # --------------------------------------------------
        # GENERATE BUTTON
        # --------------------------------------------------

        generate_button = st.button(
            "✦ Generate Email",
            type="primary",
            use_container_width=True,
        )


        # --------------------------------------------------
        # GENERATION LOGIC
        # --------------------------------------------------

        if generate_button:

            if not purpose.strip():

                st.warning(
                    "Please enter the email purpose."
                )

            elif not recipient.strip():

                st.warning(
                    "Please enter who the email is for."
                )

            elif not context.strip():

                st.warning(
                    "Please provide some context."
                )

            else:

                try:

                    prompt = build_email_prompt(
                        purpose=purpose,
                        recipient=recipient,
                        context=context,
                        tone=tone,
                        length=length,
                        key_points=key_points,
                    )


                    with st.spinner(
                        "AI is drafting your email..."
                    ):

                        result = generate_email(
                            prompt
                        )


                    st.session_state.generated_email = (
                        result
                    )


                except Exception as error:

                    st.error(
                        f"Unable to generate email: {error}"
                    )


    # ======================================================
    # REWRITE EMAIL MODE
    # ======================================================

    else:

        st.markdown(
            '<div class="panel-title">Rewrite Email</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="panel-description">
                Paste an existing email and choose how you
                want AI to improve it.
            </div>
            """,
            unsafe_allow_html=True,
        )


        # --------------------------------------------------
        # ORIGINAL EMAIL
        # --------------------------------------------------

        original_email = st.text_area(
            "Original Email",
            placeholder=(
                "Paste the email you want "
                "to improve here..."
            ),
            height=280,
        )


        # --------------------------------------------------
        # REWRITE STYLE
        # --------------------------------------------------

        rewrite_style = st.selectbox(
            "How should AI improve it?",
            [
                "Make it Professional",
                "Make it Friendly",
                "Make it Formal",
                "Make it More Polite",
                "Make it Confident",
                "Shorten it",
                "Improve Clarity",
                "Fix Grammar",
            ],
        )


        # --------------------------------------------------
        # REWRITE BUTTON
        # --------------------------------------------------

        rewrite_button = st.button(
            "✎ Rewrite Email",
            type="primary",
            use_container_width=True,
        )


        # --------------------------------------------------
        # REWRITE LOGIC
        # --------------------------------------------------

        if rewrite_button:

            if not original_email.strip():

                st.warning(
                    "Please paste an email to rewrite."
                )

            else:

                try:

                    prompt = build_rewrite_prompt(
                        email_text=original_email,
                        rewrite_style=rewrite_style,
                    )


                    with st.spinner(
                        "AI is improving your email..."
                    ):

                        result = generate_email(
                            prompt
                        )


                    st.session_state.generated_email = (
                        result
                    )


                except Exception as error:

                    st.error(
                        f"Unable to rewrite email: {error}"
                    )


# ==========================================================
# RIGHT COLUMN — AI DRAFT
# ==========================================================

with right_column:

    st.markdown(
        '<div class="panel-title">AI Draft</div>',
        unsafe_allow_html=True,
    )


    # ======================================================
    # EMAIL EXISTS
    # ======================================================

    if st.session_state.generated_email:

        st.success(
            "Draft generated successfully"
        )


        # Editable output
        edited_email = st.text_area(
            "Generated Email",
            value=st.session_state.generated_email,
            height=400,
            label_visibility="collapsed",
            key="generated_email_editor",
        )


        st.caption(
            "Review or edit your email before copying it."
        )


        # --------------------------------------------------
        # COPY SECTION
        # --------------------------------------------------

        st.markdown("##### Copy Email")


        st.code(
            edited_email,
            language=None,
        )


        st.caption(
            "Use the copy icon in the top-right corner "
            "of the box above to copy the complete email."
        )


    # ======================================================
    # EMPTY STATE
    # ======================================================

    else:

        empty_container = st.container(
            border=True,
            height=480,
        )


        with empty_container:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            st.markdown(
                "<h1 style='text-align:center;'>✦</h1>",
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <h3 style="text-align:center;">
                    Ready when you are
                </h3>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <p style="
                    text-align:center;
                    color:#8b93a7;
                ">
                    Your generated email will appear here.
                </p>
                """,
                unsafe_allow_html=True,
            )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()


st.caption(
    "AI Email Generator • AI-generated content should "
    "be reviewed before sending."
)