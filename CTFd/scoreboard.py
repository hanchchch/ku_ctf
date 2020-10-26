from flask import Blueprint, render_template

from CTFd.utils import config
from CTFd.utils.config.visibility import scores_visible
from CTFd.utils.decorators.visibility import check_score_visibility
from CTFd.utils.helpers import get_infos
from CTFd.utils.scores import get_standings, get_user_standings
from CTFd.utils.user import is_admin

scoreboard = Blueprint("scoreboard", __name__)

def set_user_rank(user_standing, rank):
    return {
        'user_id':user_standing.user_id, 
        'oauth_id':user_standing.oauth_id,
        'team_id':user_standing.team_id,
        'name':user_standing.name,
        'score':user_standing.score,
        'rank':rank
    }

@scoreboard.route("/scoreboard")
@check_score_visibility
def listing():
    infos = get_infos()

    if config.is_scoreboard_frozen():
        infos.append("Scoreboard has been frozen")

    if is_admin() is True and scores_visible() is False:
        infos.append("Scores are not currently visible to users")

    standings = get_standings()
    user_standings = get_user_standings()

    user_standings_with_rank = []
    if user_standings:

        rank = 1
        user_standings_with_rank.append(set_user_rank(user_standings[0], rank))
        for i in range(1,len(user_standings)):
            user = user_standings[i]
            pre_user = user_standings[i-1]

            if user.score < pre_user.score:
                rank += 1
            
            user_standings_with_rank.append(set_user_rank(user, rank))
        
    return render_template("scoreboard.html", standings=standings, user_standings=user_standings_with_rank, infos=infos)
