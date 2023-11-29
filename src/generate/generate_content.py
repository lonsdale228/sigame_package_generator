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


def create_lines(animes: list[Anime], questions_per_line=15, round_type=''):
    line_list = []

    if round_type not in ['voice', 'image', 'text']:
        print("Invalid round_type!")
        exit()

    while animes:
        temp_line = Line()
        temp_line.questions = []

        if len(animes) == 0:
            break

        # dry for future features
        match round_type:
            case 'image':
                for i in range(questions_per_line + 1):
                    if len(animes) == 0:
                        break
                    if animes[0] is not None:
                        temp_question = Question()
                        temp_question.price = 100
                        temp_question.type = round_type
                        temp_question.answer = animes[0].name + " / " + animes[0].name_rus
                        temp_question.hex = animes[0].hex_name
                        temp_question.ext = animes[0].scr_ext
                        temp_line.questions.append(temp_question)
                    animes.pop(0)

                line_list.append(temp_line)

            case 'voice':
                for i in range(questions_per_line + 1):
                    if len(animes) == 0:
                        break
                    temp_question = Question()
                    temp_question.price = 100
                    temp_question.type = round_type
                    temp_question.answer = animes[0].name + " / " + animes[0].name_rus
                    temp_question.hex = animes[0].hex_name
                    temp_line.questions.append(temp_question)
                    animes.pop(0)
                line_list.append(temp_line)

    return line_list


def create_rounds(animes, line_limit, per_line_limit , round_type):
    line_name = "Default"
    round_name = "Default round"
    match round_type:
        case 'voice':
            round_name = "Openings"
            line_name = 'OP'
        case 'image':
            round_name = "Screenshots"
            line_name = 'Screenshots'

    line_list = create_lines(animes, per_line_limit, round_type)
    for i, line in enumerate(line_list):
        line.name = f"{line_name} {i + 1}"

    round_list = []

    while line_list:
        temp_round = Round()
        temp_round.lines = []
        temp_round.name = round_name

        for i in range(line_limit):
            if len(line_list) == 0:
                break
            temp_round.lines.append(line_list[0])
            line_list.pop(0)

        round_list.append(temp_round)

    return round_list


# def create_xml_round(round_list: list) -> list:
#
#     xml_rounds_list = []
#     for i, round in enumerate(round_list):
#         xml_round = ET.Element("round", name=f'{round.name} {i}')
#         xml_themes = ET.SubElement(xml_round, "themes")
#         for line in round.lines:
#             if line.questions:
#                 xml_line = ET.SubElement(xml_themes, "theme", name=line.name)
#                 xml_questions = ET.SubElement(xml_line, "questions")
#                 for question in line.questions:
#                     xml_que = ET.SubElement(xml_questions, "question", price=f"{question.price}")
#                     xml_scenario = ET.SubElement(xml_que, "scenario")
#                     xml_atom_type = ET.SubElement(xml_scenario, "atom", type=f"{question.type}")
#                     match question.type:
#                         case "voice":
#                             xml_atom_type.text = "@" + question.hex + ".m4a"
#                         case "image":
#                             xml_atom_type.text = "@" + question.hex + question.ext
#                         case "video":
#                             xml_atom_type.text = "@" + question.hex + ".mp4"
#                     xml_right = ET.SubElement(xml_que, "right")
#                     xml_answer = ET.SubElement(xml_right, "answer")
#
#                     xml_answer.text = question.answer
#         xml_rounds_list.append(xml_round)
#     return xml_rounds_list


def create_xml_rounds(round_list: list, shuffle_lines: bool = True, shuffle_questions: bool = True) -> list:
    xml_rounds_list = []

    import random
    if shuffle_lines:
        all_lines = []
        for anime_round in round_list:
            all_lines = all_lines + anime_round.lines
        max_num = max(len(i.lines) for i in round_list)

        random.shuffle(all_lines)

        start_index = 0
        for anime_round in round_list:
            anime_round.lines = all_lines[start_index:start_index + max_num]
            start_index += max_num

        for anime_round in round_list:
            anime_round.name = "Shuffled lines"

    if shuffle_questions:
        all_questions = []
        for anime_round in round_list:
            for line in anime_round.lines:
                all_questions = all_questions + line.questions
        random.shuffle(all_questions)

        question_index = 0

        for anime_round in round_list:
            for line in anime_round.lines:
                question_count = len(line.questions)
                line.questions = all_questions[question_index:question_index + question_count]
                question_index += question_count

        for anime_round in round_list:
            for line in anime_round.lines:
                line.name = "Shuffled questions"

    for i, round in enumerate(round_list):
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
                    match question.type:
                        case "voice":
                            xml_atom_type.text = "@" + question.hex + ".mp3"
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
