{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "mount_file_id": "1vGu3wYxOxXwwdXGisMtNN9jlcDo4spOC",
      "authorship_tag": "ABX9TyMlRokpHwEaS/Tm19Mc9U/S",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/bitsg74/dsad18/blob/main/ps18.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bTFnvJEHIGVB",
        "outputId": "b834262e-0390-45f6-e6cb-0d9436c70c42"
      },
      "source": [
        "\"\"\"Group 74 - DSAD Assignment - PS18, Hash table implementation assignment\"\"\"\r\n",
        "\r\n",
        "def initializeHash(self):\r\n",
        "  \"\"\"This function creates an empty hash table and points to null \"\"\"\r\n",
        "  pass\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "def insertStudentRec(StudentHashRecords, studentId, CGPA):\r\n",
        "  \"\"\"\r\n",
        "  This function inserts the student id and corresponding CPGA into the \r\n",
        "  hash table. \r\n",
        "  The inputs need to be read from a file inputPS18.txt which contains the \r\n",
        "  student ID and overall graduating CGPA \r\n",
        "  (decimal value with a maximum of 5.0 points). \r\n",
        "  The file read can happen outside the function and only the\r\n",
        "  information in every individual row needs to be passed to the function.\r\n",
        "  \"\"\"\r\n",
        "  pass\r\n",
        "\r\n",
        "def hallOfFame(StudentHashRecords): \r\n",
        "  \"\"\"\r\n",
        "  This function prints the list of all students who have\r\n",
        "  graduated and topped their department in their year of graduation \r\n",
        "  (Only students who graduated should be considered. \r\n",
        "  Calculate the applicable year range accordingly). \r\n",
        "  The trigger can be read from the file promptsPS18.txt. \r\n",
        "  The input can be identified with the tag --> hallOfFame:\r\n",
        "  \"\"\"\r\n",
        "  pass\r\n",
        "\r\n",
        "\r\n",
        "def newCourseList(StudentHashRecords, CGPAFrom, CPGATo): \r\n",
        "  \"\"\"\r\n",
        "  This function prints the\r\n",
        "  list of all students who have a CGPA within the given range and have \r\n",
        "  graduated in the last 5 years (Only students who graduated should be \r\n",
        "  considered. Calculate the applicable year range accordingly). \r\n",
        "  The input CGPAs can be read from the file promptsPS18.txt. The input\r\n",
        "  can be identified with the tag mentioned below -\r\n",
        "  courseOffer: 3.5 : 4.0\r\n",
        "  \"\"\"\r\n",
        "  pass\r\n",
        "\r\n",
        "\r\n",
        "def depAvg(StudentHashRecords): \r\n",
        "  \"\"\"\r\n",
        "  This function prints the list of all departments followed\r\n",
        "  by the maximum CGPA and average CGPA of all students in that department. \r\n",
        "  The output should be captured in outputPS18.txt following format\r\n",
        "  Output format:\r\n",
        "  ---------- department CGPA ----------\r\n",
        "  CSE: max: 3.5, avg: 3.4\r\n",
        "  MEC: max: 3.5, avg: 3.4\r\n",
        "  ECE: max: 3.5, avg: 3.4\r\n",
        "  ARC: max: 3.5, avg: 3.4\r\n",
        "  -------------------------------------\r\n",
        "  \"\"\"\r\n",
        "  pass\r\n",
        "\r\n",
        "def destroyHash(StudentHashRecords): \r\n",
        "  \"\"\"\r\n",
        "  This function destroys all the entries inside hash\r\n",
        "  table. This is a clean-up code.\r\n",
        "  \"\"\"\r\n",
        "  pass\r\n",
        "\r\n",
        "def helperFunction():\r\n",
        "  \"\"\"\r\n",
        "  Custom function for error checking\r\n",
        "  \"\"\"\r\n",
        "  pass\r\n",
        "\r\n",
        "f=open('inputPS18.txt','r')\r\n",
        "print(f.read())\r\n",
        "print(insertStudentRec.__doc__)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "2010CSE1223 / 3.5\n",
            "2010CSE1224 / 3.9\n",
            "2010CSE1225 / 4.5\n",
            "2010CSE1226 / 4.8\n",
            "2010CSE1227 / 4.1\n",
            "2010MEC1001 / 4.2\n",
            "\n",
            "  This function inserts the student id and corresponding CPGA into the hash table. \n",
            "  The inputs need to be read from a file inputPS18.txt which contains the \n",
            "  student ID and overall graduating CGPA \n",
            "  (decimal value with a maximum of 5.0 points). \n",
            "  The file read can happen outside the function and only the\n",
            "  information in every individual row needs to be passed to the function.\n",
            "  \n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}