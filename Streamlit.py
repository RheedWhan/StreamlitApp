{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1NZjfbsEu9kXQqqy9rAbgcVG6bWIY_90m",
      "authorship_tag": "ABX9TyM/VnZ4+q4otPtTpEVk5G5g",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/RheedWhan/StreamlitApp/blob/main/Streamlit.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h8WAIjH6_Du8",
        "outputId": "acba1918-7c09-4209-c983-7ee97e5f8100"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JFgjsVY12qKw",
        "outputId": "62480f8d-1db5-478a-874f-6a0ace894747"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "35.245.236.137\n",
            "[##................] / fetchMetadata: sill resolveWithNewModule ms@2.1.2 checki\u001b[0m\u001b[K\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.\n",
            "\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://35.245.236.137:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[K\u001b[?25hnpx: installed 22 in 6.999s\n",
            "your url is: https://loud-impalas-eat.loca.lt\n"
          ]
        }
      ],
      "source": [
        "! pip install streamlit -q\n",
        "!wget -q -O - ipv4.icanhazip.com\n",
        "! streamlit run app.py & npx localtunnel --port 8501"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "st.write('# Streamlit calculator')\n",
        "number1= st.number_input('number 1')\n",
        "number2 = st.number_input('number 2')\n",
        "num3 = number1+number2\n",
        "st.write('# Answer is ',num3)"
      ],
      "metadata": {
        "id": "FqnEGiRz3crk"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "nRvpBtb_6bJh"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}