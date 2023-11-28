import secrets
import xml.etree.ElementTree as ET
from src.entities.rounds import Question, Line, Round
from src.entities.anime import Anime

m_encoding = 'UTF-8'

package = ET.Element("package")
package.set("name", "beba")
package.set("version", "4")
id = secrets.token_hex(32)
package.set("id", id)
package.set("date", "01.01.2001")
package.set("publisher", "beba")
package.set("difficulty", "5")
package.set("xmlns", "http://vladimirkhil.com/ygpackage3.0.xsd")

info = ET.SubElement(package, "info")

authors = ET.SubElement(info, "authors")
author = ET.SubElement(authors, "author").text = "bibaiboba"
comments = ET.SubElement(info, "comments").text = "_"

rounds = ET.SubElement(package, "rounds")

# numOfQuestions = 300
# rounds_num = numOfQuestions // 100
# for i in range(rounds_num):
#     round = ET.SubElement(rounds, "round")
#     themes = ET.SubElement(round, "themes")


# def create_screenshot_line(animes: list[Anime], limit=15):
#     temp_line = line()
#     temp_line.questions = []
#
#     for i in range(limit):
#         temp_question = question()
#         temp_question.price = 100
#         temp_question.type = "image"
#         try:
#             if animes[0].screenshots != None:
#                 temp_question.answer = animes[0].name + " / " + animes[0].name_rus
#                 temp_question.hex = animes[0].hex_name
#                 temp_question.ext = animes[0].scr_ext
#                 temp_line.questions.append(temp_question)
#             animes.pop(0)
#
#         except IndexError:
#             ...
#
#         if len(animes) == 0: return temp_line
#     return temp_line


def create_screenshot_lines(animes: list[Anime], questions_per_line=15):
    line_list=[]
    while animes:
        temp_line=Line()
        temp_line.questions = []

        if len(animes)==0:
            break

        if animes[0].screenshots is not None:

            for i in range(questions_per_line+1):
                if len(animes) == 0:
                    break
                temp_question = Question()
                temp_question.price = 100
                temp_question.type = "image"
                temp_question.answer = animes[0].name + " / " + animes[0].name_rus
                temp_question.hex = animes[0].hex_name
                temp_question.ext = animes[0].scr_ext
                temp_line.questions.append(temp_question)
                animes.pop(0)

            line_list.append(temp_line)

    return line_list

def create_audio_line(animes, limit=15):
    temp_line = Line()
    temp_line.questions = []

    for i in range(limit):
        temp_question = Question()
        temp_question.price = 100
        temp_question.type = "voice"
        try:
            temp_question.answer = animes[0].name + " / " + animes[0].name_rus
            temp_question.hex = animes[0].hex_name
            temp_line.questions.append(temp_question)
            animes.pop(0)
        except IndexError:
            ...

        if len(animes) == 0:
            return temp_line

    return temp_line


def create_scr_rounds(animes, line_limit=10):

    line_list=create_screenshot_lines(animes)
    for i, line in enumerate(line_list):
        line.name = f"Screenshots {i+1}"

    round_list=[]
    while line_list:
        temp_round = Round()
        temp_round.lines = []
        temp_round.name = "Screenshots"

        for i in range(line_limit):
            if len(line_list) == 0:
                break
            temp_round.lines.append(line_list[0])
            line_list.pop(0)

        round_list.append(temp_round)

    return round_list


def create_round(animes, limit=10):
    temp_round = Round()
    temp_round.lines = []
    temp_round.name = "Openings"
    for i in range(limit):
        temp_round.lines.append(create_audio_line(animes))
        temp_round.lines[i].name = f"OP {i + 1}"
    return temp_round


def create_xml_round(round_list, type):
    xml_rounds_list=[]
    for i,round in enumerate(round_list):
        xml_round = ET.Element("round", name=f'{round.name} {i}')
        xml_themes = ET.SubElement(xml_round, "themes")
        for line in round.lines:
            if line.questions:
                xml_line = ET.SubElement(xml_themes, "theme", name=line.name)
                xml_questions = ET.SubElement(xml_line, "questions")
                for question in line.questions:
                    xml_que = ET.SubElement(xml_questions, "question", price=f"{question.price}")
                    xml_scenario = ET.SubElement(xml_que, "scenario")
                    xml_atom_type = ET.SubElement(xml_scenario, "atom", type=f"{question.type}")
                    match type:
                        case "audio":
                            xml_atom_type.text = "@" + question.hex + ".m4a"
                        case "image":
                            xml_atom_type.text = "@" + question.hex + question.ext
                        case "video":
                            xml_atom_type.text = "@" + question.hex + ".mp4"
                    xml_right = ET.SubElement(xml_que, "right")
                    xml_answer = ET.SubElement(xml_right, "answer")
                    xml_answer.text = question.answer
        xml_rounds_list.append(xml_round)
    return xml_rounds_list


def create_xml(xml_round_list: list, nickname: str):
    from datetime import datetime
    package_name = f"Animes of {nickname}"
    package_id = secrets.token_hex(16)
    root = ET.Element("package", {
        "name": package_name,
        "version": "4",
        "id": f"{package_id}",
        "date": f"{datetime.now().strftime('%d.%m.%Y')}",
        "publisher": "bibaiboba",
        "difficulty": "5",
        "xmlns": "http://vladimirkhil.com/ygpackage3.0.xsd"
    })
    round_list = ET.SubElement(root, "rounds")

    for xml_round in xml_round_list:
        round_list.append(xml_round)
    tree = ET.ElementTree(root)

    tree.write("temp\\" + "content.xml", encoding="utf-8", xml_declaration=True)

