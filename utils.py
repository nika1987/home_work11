import json
import os
from constants import DATA_FILE

def load_candidates_from_json(path):
    """
     функция возвращает список всех кандидатов
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def get_candidate(candidate_id):
    """
    функция возвращает одного кандидата по его id
    """
    for candidate in load_candidates_from_json(DATA_FILE):
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """
    функция возвращает кандидатов по имени
    """
    name = []
    for candidate in load_candidates_from_json(DATA_FILE):
        if candidate_name.lower() in candidate["name"].lower():
            name.append(candidate)
    return name


def get_candidates_by_skill(skill_name):
    """
    функция возвращает кандидатов по навыку
    """
    skill = []
    for candidate in load_candidates_from_json(DATA_FILE):
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            skill.append(candidate)
    return skill
