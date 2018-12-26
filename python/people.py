idols = {
    "black mamba":{
        "first":"kobe",
        "last":"bryant",
        "team":"los angeles lakers",
    },
    "king":{
        "first":"lebron",
        "last":"james",
        "team":"cleveland cavaliers",
    },
    "melo":{
        "first":"carmelo",
        "last":"anthony",
        "team":"new york knicks"
    }


}
for nick_name,idol_info in idols.items():
    print("\nIdol:" + nick_name.title())
    full_name = idol_info["first"]  + " " + idol_info["last"]
    team = idol_info["team"]

    print("\tFull name: " + full_name.title())
    print("\tTeam: " + team.title())