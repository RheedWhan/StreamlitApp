{
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
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h8WAIjH6_Du8",
        "outputId": "5b5dd9d6-f0ef-459c-9033-ef9b0485a0d5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "st.write('# Streamlit calculator')\n",
        "number1= st.number_input('number 1')\n",
        "number2 = st.number_input('number 2')\n",
        "num3 = number1+number2\n",
        "st.write('# Answer is ',num3)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JFgjsVY12qKw",
        "outputId": "182ec75c-287e-4fa6-a280-97765a490ffd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.4/8.4 MB\u001b[0m \u001b[31m14.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m190.6/190.6 kB\u001b[0m \u001b[31m10.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.8/4.8 MB\u001b[0m \u001b[31m34.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m82.1/82.1 kB\u001b[0m \u001b[31m6.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m6.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting pyngrok\n",
            "  Downloading pyngrok-7.0.5-py3-none-any.whl (21 kB)\n",
            "Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from pyngrok) (6.0.1)\n",
            "Installing collected packages: pyngrok\n",
            "Successfully installed pyngrok-7.0.5\n"
          ]
        }
      ],
      "source": [
        "! pip install streamlit -q\n",
        "! pip install --upgrade streamlit -q\n",
        "! pip install pyngrok"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HH42oCR1IY-3",
        "outputId": "874f9b20-a855-4cad-ed23-b65d99078f0b"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "app.py\tdrive  sample_data\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ngrok"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k14s-B8eJNN2",
        "outputId": "23196ee1-0983-49dc-c286-155ef1697cf8"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "NAME:\n",
            "  ngrok - tunnel local ports to public URLs and inspect traffic\n",
            "\n",
            "USAGE:\n",
            "  ngrok [command] [flags]\n",
            "\n",
            "DESCRIPTION: \n",
            "  ngrok exposes local networked services behinds NATs and firewalls to the\n",
            "  public internet over a secure tunnel. Share local websites, build/test\n",
            "  webhook consumers and self-host personal services.\n",
            "  Detailed help for each command is available with 'ngrok help <command>'.\n",
            "  Open http://localhost:4040 for ngrok's web interface to inspect traffic.\n",
            "\n",
            "Author:\n",
            "  ngrok - <support@ngrok.com>\n",
            "\n",
            "TERMS OF SERVICE: https://ngrok.com/tos\n",
            "\n",
            "EXAMPLES: \n",
            "  ngrok http 80                           # secure public URL for port 80 web server\n",
            "  ngrok http --domain baz.ngrok.dev 8080  # port 8080 available at baz.ngrok.dev\n",
            "  ngrok http foo.dev:80                   # tunnel to host:port instead of localhost\n",
            "  ngrok http https://localhost            # expose a local https server\n",
            "  ngrok tcp 22                            # tunnel arbitrary TCP traffic to port 22\n",
            "  ngrok tls --domain=foo.com 443          # TLS traffic for foo.com to port 443\n",
            "  ngrok start foo bar baz                 # start tunnels from the configuration file\n",
            "\n",
            "COMMANDS:\n",
            "  api                            use ngrok agent as an api client\n",
            "  completion                     generates shell completion code for bash or zsh\n",
            "  config                         update or migrate ngrok's configuration file\n",
            "  credits                        prints author and licensing information\n",
            "  diagnose                       diagnose connection issues\n",
            "  help                           Help about any command\n",
            "  http                           start an HTTP tunnel\n",
            "  service                        run and control an ngrok service on a target operating system\n",
            "  start                          start tunnels by name from the configuration file\n",
            "  tcp                            start a TCP tunnel\n",
            "  tls                            start a TLS tunnel\n",
            "  tunnel                         start a tunnel for use with a tunnel-group backend\n",
            "  update                         update ngrok to the latest version\n",
            "  version                        print the version string\n",
            "\n",
            "OPTIONS:\n",
            "      --config strings    path to config files; they are merged if multiple\n",
            "  -h, --help              help for ngrok\n",
            "      --metadata string   opaque user-defined metadata for the tunnel session\n",
            "  -v, --version           version for ngrok\n",
            "\n",
            "PYNGROK VERSION:\n",
            "   7.0.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ngrok config add-authtoken 2aN81VhyReLGZ4nWjIS8n8JjrqL_jZRmXKTfcABbftoU8tFH"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x8ey4VTYJTDg",
        "outputId": "031b5655-df7d-487e-96bd-c9fb2e849912"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Authtoken saved to configuration file: /root/.config/ngrok/ngrok.yml\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ngrok"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gLwJx-leJmhg",
        "outputId": "24bf792f-dcc9-4a37-f7fd-b8c046eba622"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "NAME:\n",
            "  ngrok - tunnel local ports to public URLs and inspect traffic\n",
            "\n",
            "USAGE:\n",
            "  ngrok [command] [flags]\n",
            "\n",
            "DESCRIPTION: \n",
            "  ngrok exposes local networked services behinds NATs and firewalls to the\n",
            "  public internet over a secure tunnel. Share local websites, build/test\n",
            "  webhook consumers and self-host personal services.\n",
            "  Detailed help for each command is available with 'ngrok help <command>'.\n",
            "  Open http://localhost:4040 for ngrok's web interface to inspect traffic.\n",
            "\n",
            "Author:\n",
            "  ngrok - <support@ngrok.com>\n",
            "\n",
            "TERMS OF SERVICE: https://ngrok.com/tos\n",
            "\n",
            "EXAMPLES: \n",
            "  ngrok http 80                           # secure public URL for port 80 web server\n",
            "  ngrok http --domain baz.ngrok.dev 8080  # port 8080 available at baz.ngrok.dev\n",
            "  ngrok http foo.dev:80                   # tunnel to host:port instead of localhost\n",
            "  ngrok http https://localhost            # expose a local https server\n",
            "  ngrok tcp 22                            # tunnel arbitrary TCP traffic to port 22\n",
            "  ngrok tls --domain=foo.com 443          # TLS traffic for foo.com to port 443\n",
            "  ngrok start foo bar baz                 # start tunnels from the configuration file\n",
            "\n",
            "COMMANDS:\n",
            "  api                            use ngrok agent as an api client\n",
            "  completion                     generates shell completion code for bash or zsh\n",
            "  config                         update or migrate ngrok's configuration file\n",
            "  credits                        prints author and licensing information\n",
            "  diagnose                       diagnose connection issues\n",
            "  help                           Help about any command\n",
            "  http                           start an HTTP tunnel\n",
            "  service                        run and control an ngrok service on a target operating system\n",
            "  start                          start tunnels by name from the configuration file\n",
            "  tcp                            start a TCP tunnel\n",
            "  tls                            start a TLS tunnel\n",
            "  tunnel                         start a tunnel for use with a tunnel-group backend\n",
            "  update                         update ngrok to the latest version\n",
            "  version                        print the version string\n",
            "\n",
            "OPTIONS:\n",
            "      --config strings    path to config files; they are merged if multiple\n",
            "  -h, --help              help for ngrok\n",
            "      --metadata string   opaque user-defined metadata for the tunnel session\n",
            "  -v, --version           version for ngrok\n",
            "\n",
            "PYNGROK VERSION:\n",
            "   7.0.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from pyngrok import ngrok"
      ],
      "metadata": {
        "id": "m-YK3G9_JmdC"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app.py&>/dev/null&"
      ],
      "metadata": {
        "id": "-lQqR0FGKjxl"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "port_url ="
      ],
      "metadata": {
        "id": "xS-n1Mh7JmZG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "C2SMIUniJmVG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "FqnEGiRz3crk"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "st.write('# Streamlit calculator')\n",
        "number1= st.number_input('number 1')\n",
        "number2 = st.number_input('number 2')\n",
        "num3 = number1+number2\n",
        "st.write('# Answer is ',num3)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "nRvpBtb_6bJh"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1NZjfbsEu9kXQqqy9rAbgcVG6bWIY_90m",
      "authorship_tag": "ABX9TyMJhF6gd8SO/BXL4Yt4lnnq",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}