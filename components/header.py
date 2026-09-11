import base64
from pathlib import Path

import streamlit as st


def show_header():

    logo = Path("www/assets/logo.png")

    logo_html = ""

    if logo.exists():

        encoded_logo = base64.b64encode(
            logo.read_bytes()
        ).decode()

        logo_html = f"""
        <img
            src="data:image/png;base64,{encoded_logo}"
            class="header-logo"
        >
        """

    st.html(
        f"""
        <div class="top-header">

            <div class="header-left">

                <div class="header-logo-wrapper">
                    {logo_html}
                </div>

                <div class="header-text">

                    <div class="header-title">
                        Mushaki AI
                    </div>

                    <div class="header-subtitle">
                        Your intelligent personal AI assistant
                    </div>

                </div>

            </div>

            <div class="header-status">

                <span class="header-status-dot"></span>

                Online

            </div>

        </div>
        """
    )