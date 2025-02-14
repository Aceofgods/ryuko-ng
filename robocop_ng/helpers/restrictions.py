import json
import os


def get_restrictions_path(bot):
    return os.path.join(bot.state_dir, "data/restrictions.json")


def get_restrictions(bot):
    with open(get_restrictions_path(bot), "r") as f:
        return json.load(f)


def set_restrictions(bot, contents):
    with open(get_restrictions_path(bot), "w") as f:
        f.write(contents)


def get_user_restrictions(bot, uid):
    uid = str(uid)
    with open(get_restrictions_path(bot), "r") as f:
        rsts = json.load(f)
        if uid in rsts:
            return rsts[uid]
        return []


def add_restriction(bot, uid, rst):
    # mostly from kurisu source, credits go to ihaveamac
    uid = str(uid)
    rsts = get_restrictions(bot)
    if uid not in rsts:
        rsts[uid] = []
    if rst not in rsts[uid]:
        rsts[uid].append(rst)
    set_restrictions(bot, json.dumps(rsts))


def remove_restriction(bot, uid, rst):
    # mostly from kurisu source, credits go to ihaveamac
    uid = str(uid)
    rsts = get_restrictions(bot)
    if uid not in rsts:
        rsts[uid] = []
    if rst in rsts[uid]:
        rsts[uid].remove(rst)
    set_restrictions(bot, json.dumps(rsts))
