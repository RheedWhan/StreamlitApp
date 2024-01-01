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
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h8WAIjH6_Du8",
        "outputId": "66829f16-f047-48a7-8559-2fd7986d692b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "PAGE_CONFIG = {\"page_title\":\"StColab.io\",\"page_icon\":\":smiley:\",\"layout\":\"centered\"}\n",
        "st.beta_set_page_config(**PAGE_CONFIG)\n",
        "\n",
        "\n",
        "def main():\n",
        "\tst.title(\"Awesome Streamlit for ML\")\n",
        "\tst.subheader(\"How to run streamlit from colab\")\n",
        "\n",
        "\n",
        "\tmenu = [\"Home\",\"About\"]\n",
        "\tchoice = st.sidebar.selectbox('Menu',menu)\n",
        "\tif choice == 'Home':\n",
        "\t\tst.subheader(\"Streamlit From Colab\")\n",
        "\n",
        "\n",
        "\n",
        "if __name__ == '__main__':\n",
        "\tmain()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JFgjsVY12qKw",
        "outputId": "0d668f9a-4fb2-4db6-f3e2-cb2ecb3fc42f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: pyngrok in /usr/local/lib/python3.10/dist-packages (7.0.5)\n",
            "Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from pyngrok) (6.0.1)\n"
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
        "outputId": "ae6fd385-463e-4a09-8bb7-8e9847c1f2d0"
      },
      "execution_count": 22,
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
        "outputId": "c03f584a-0234-443b-b364-276045ddd0eb"
      },
      "execution_count": 23,
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
        "outputId": "bd2831f9-3e16-49ff-a894-34cb08e8fb04"
      },
      "execution_count": 24,
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
        "outputId": "0529c4f4-3d8d-4983-d673-6bc320dca612"
      },
      "execution_count": 25,
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
        "import logging\n",
        "import sys\n",
        "from pyngrok import ngrok, process\n",
        "\n",
        "root = logging.getLogger()\n",
        "root.setLevel(logging.DEBUG)\n",
        "handler = logging.StreamHandler(sys.stdout)\n",
        "handler.setLevel(logging.DEBUG)\n",
        "formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')\n",
        "handler.setFormatter(formatter)\n",
        "root.addHandler(handler)"
      ],
      "metadata": {
        "id": "m-YK3G9_JmdC"
      },
      "execution_count": 33,
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
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pgrep streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "etf7GNWzLMzL",
        "outputId": "1febe40f-58e0-48bf-822a-c96fc4b468bd"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "11029\n",
            "15173\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "publ_url = ngrok.connect(port='8501')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 845
        },
        "id": "xS-n1Mh7JmZG",
        "outputId": "751a9816-212c-4f40-8b67-0d5c54eb709c"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "INFO:pyngrok.ngrok:Opening tunnel named: http-80-c3c64bf5-f1be-4d40-a6f9-057cb17a555a\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2024-01-01 23:23:43,372 - pyngrok.ngrok - INFO - Opening tunnel named: http-80-c3c64bf5-f1be-4d40-a6f9-057cb17a555a\n",
            "2024-01-01 23:23:43,372 - pyngrok.ngrok - INFO - Opening tunnel named: http-80-c3c64bf5-f1be-4d40-a6f9-057cb17a555a\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "DEBUG:pyngrok.ngrok:Creating tunnel with options: {'port': '8501', 'name': 'http-80-c3c64bf5-f1be-4d40-a6f9-057cb17a555a', 'addr': '80', 'proto': 'http'}\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2024-01-01 23:23:43,379 - pyngrok.ngrok - DEBUG - Creating tunnel with options: {'port': '8501', 'name': 'http-80-c3c64bf5-f1be-4d40-a6f9-057cb17a555a', 'addr': '80', 'proto': 'http'}\n",
            "2024-01-01 23:23:43,379 - pyngrok.ngrok - DEBUG - Creating tunnel with options: {'port': '8501', 'name': 'http-80-c3c64bf5-f1be-4d40-a6f9-057cb17a555a', 'addr': '80', 'proto': 'http'}\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "DEBUG:pyngrok.ngrok:Making POST request to http://127.0.0.1:4040/api/tunnels with data: {'port': '8501', 'name': 'http-80-c3c64bf5-f1be-4d40-a6f9-057cb17a555a', 'addr': '80', 'proto': 'http'}\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2024-01-01 23:23:43,382 - pyngrok.ngrok - DEBUG - Making POST request to http://127.0.0.1:4040/api/tunnels with data: {'port': '8501', 'name': 'http-80-c3c64bf5-f1be-4d40-a6f9-057cb17a555a', 'addr': '80', 'proto': 'http'}\n",
            "2024-01-01 23:23:43,382 - pyngrok.ngrok - DEBUG - Making POST request to http://127.0.0.1:4040/api/tunnels with data: {'port': '8501', 'name': 'http-80-c3c64bf5-f1be-4d40-a6f9-057cb17a555a', 'addr': '80', 'proto': 'http'}\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "INFO:pyngrok.process.ngrok:t=2024-01-01T23:23:43+0000 lvl=info msg=start pg=/api/tunnels id=c1169c4651999d60\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2024-01-01 23:23:43,388 - pyngrok.process.ngrok - INFO - t=2024-01-01T23:23:43+0000 lvl=info msg=start pg=/api/tunnels id=c1169c4651999d60\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "DEBUG:pyngrok.ngrok:Response 400: {\"error_code\":102,\"status_code\":400,\"msg\":\"invalid tunnel configuration\",\"details\":{\"err\":\"yaml: unmarshal errors:\\n  line 1: field port not found in type config.HTTPv2Tunnel\"}}\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2024-01-01 23:23:43,388 - pyngrok.process.ngrok - INFO - t=2024-01-01T23:23:43+0000 lvl=info msg=start pg=/api/tunnels id=c1169c4651999d60\n",
            "2024-01-01 23:23:43,390 - pyngrok.ngrok - DEBUG - Response 400: {\"error_code\":102,\"status_code\":400,\"msg\":\"invalid tunnel configuration\",\"details\":{\"err\":\"yaml: unmarshal errors:\\n  line 1: field port not found in type config.HTTPv2Tunnel\"}}\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:pyngrok.process.ngrok:t=2024-01-01T23:23:43+0000 lvl=warn msg=\"invalid tunnel configuration\" pg=/api/tunnels id=c1169c4651999d60 err=\"yaml: unmarshal errors:\\n  line 1: field port not found in type config.HTTPv2Tunnel\"\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2024-01-01 23:23:43,390 - pyngrok.ngrok - DEBUG - Response 400: {\"error_code\":102,\"status_code\":400,\"msg\":\"invalid tunnel configuration\",\"details\":{\"err\":\"yaml: unmarshal errors:\\n  line 1: field port not found in type config.HTTPv2Tunnel\"}}\n",
            "2024-01-01 23:23:43,396 - pyngrok.process.ngrok - WARNING - t=2024-01-01T23:23:43+0000 lvl=warn msg=\"invalid tunnel configuration\" pg=/api/tunnels id=c1169c4651999d60 err=\"yaml: unmarshal errors:\\n  line 1: field port not found in type config.HTTPv2Tunnel\"\n",
            "2024-01-01 23:23:43,396 - pyngrok.process.ngrok - WARNING - t=2024-01-01T23:23:43+0000 lvl=warn msg=\"invalid tunnel configuration\" pg=/api/tunnels id=c1169c4651999d60 err=\"yaml: unmarshal errors:\\n  line 1: field port not found in type config.HTTPv2Tunnel\"\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "INFO:pyngrok.process.ngrok:t=2024-01-01T23:23:43+0000 lvl=info msg=end pg=/api/tunnels id=c1169c4651999d60 status=400 dur=968.035µs\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2024-01-01 23:23:43,417 - pyngrok.process.ngrok - INFO - t=2024-01-01T23:23:43+0000 lvl=info msg=end pg=/api/tunnels id=c1169c4651999d60 status=400 dur=968.035µs\n",
            "2024-01-01 23:23:43,417 - pyngrok.process.ngrok - INFO - t=2024-01-01T23:23:43+0000 lvl=info msg=end pg=/api/tunnels id=c1169c4651999d60 status=400 dur=968.035µs\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "PyngrokNgrokHTTPError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mHTTPError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pyngrok/ngrok.py\u001b[0m in \u001b[0;36mapi_request\u001b[0;34m(url, method, data, params, timeout, auth)\u001b[0m\n\u001b[1;32m    506\u001b[0m     \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 507\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0murlopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mencoded_data\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    508\u001b[0m         \u001b[0mresponse_data\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdecode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"utf-8\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/urllib/request.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(url, data, timeout, cafile, capath, cadefault, context)\u001b[0m\n\u001b[1;32m    215\u001b[0m         \u001b[0mopener\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_opener\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 216\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0mopener\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    217\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/urllib/request.py\u001b[0m in \u001b[0;36mopen\u001b[0;34m(self, fullurl, data, timeout)\u001b[0m\n\u001b[1;32m    524\u001b[0m             \u001b[0mmeth\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprocessor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmeth_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 525\u001b[0;31m             \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmeth\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    526\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/urllib/request.py\u001b[0m in \u001b[0;36mhttp_response\u001b[0;34m(self, request, response)\u001b[0m\n\u001b[1;32m    633\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;36m200\u001b[0m \u001b[0;34m<=\u001b[0m \u001b[0mcode\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0;36m300\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 634\u001b[0;31m             response = self.parent.error(\n\u001b[0m\u001b[1;32m    635\u001b[0m                 'http', request, response, code, msg, hdrs)\n",
            "\u001b[0;32m/usr/lib/python3.10/urllib/request.py\u001b[0m in \u001b[0;36merror\u001b[0;34m(self, proto, *args)\u001b[0m\n\u001b[1;32m    562\u001b[0m             \u001b[0margs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mdict\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'default'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'http_error_default'\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0morig_args\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 563\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_call_chain\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    564\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/urllib/request.py\u001b[0m in \u001b[0;36m_call_chain\u001b[0;34m(self, chain, kind, meth_name, *args)\u001b[0m\n\u001b[1;32m    495\u001b[0m             \u001b[0mfunc\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhandler\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmeth_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 496\u001b[0;31m             \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    497\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mresult\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/urllib/request.py\u001b[0m in \u001b[0;36mhttp_error_default\u001b[0;34m(self, req, fp, code, msg, hdrs)\u001b[0m\n\u001b[1;32m    642\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mhttp_error_default\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreq\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcode\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhdrs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 643\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mHTTPError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfull_url\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcode\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhdrs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    644\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mHTTPError\u001b[0m: HTTP Error 400: Bad Request",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mPyngrokNgrokHTTPError\u001b[0m                     Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-37-82e02cced424>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mpubl_url\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mngrok\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mport\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'8501'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pyngrok/ngrok.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(addr, proto, name, pyngrok_config, **options)\u001b[0m\n\u001b[1;32m    311\u001b[0m     \u001b[0mlogger\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Creating tunnel with options: {}\"\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moptions\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    312\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 313\u001b[0;31m     tunnel = NgrokTunnel(api_request(\"{}/api/tunnels\".format(api_url), method=\"POST\", data=options,\n\u001b[0m\u001b[1;32m    314\u001b[0m                                      timeout=pyngrok_config.request_timeout),\n\u001b[1;32m    315\u001b[0m                          pyngrok_config, api_url)\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pyngrok/ngrok.py\u001b[0m in \u001b[0;36mapi_request\u001b[0;34m(url, method, data, params, timeout, auth)\u001b[0m\n\u001b[1;32m    526\u001b[0m         \u001b[0mlogger\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Response {}: {}\"\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mstatus_code\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresponse_data\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstrip\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    527\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 528\u001b[0;31m         raise PyngrokNgrokHTTPError(\"ngrok client exception, API returned {}: {}\".format(status_code, response_data),\n\u001b[0m\u001b[1;32m    529\u001b[0m                                     \u001b[0me\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    530\u001b[0m                                     status_code, e.reason, e.headers, response_data)\n",
            "\u001b[0;31mPyngrokNgrokHTTPError\u001b[0m: ngrok client exception, API returned 400: {\"error_code\":102,\"status_code\":400,\"msg\":\"invalid tunnel configuration\",\"details\":{\"err\":\"yaml: unmarshal errors:\\n  line 1: field port not found in type config.HTTPv2Tunnel\"}}\n"
          ]
        }
      ]
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
        "'''import streamlit as st\n",
        "st.write('# Streamlit calculator')\n",
        "number1= st.number_input('number 1')\n",
        "number2 = st.number_input('number 2')\n",
        "num3 = number1+number2\n",
        "st.write('# Answer is ',num3)'''"
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
      "authorship_tag": "ABX9TyP+xqC5hOOEXuFEgPFPKiDo",
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