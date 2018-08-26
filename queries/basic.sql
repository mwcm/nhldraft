SELECT fname, lname, average_pick, o_rank, season_stats, projected_stats FROM nhl.players
where average_round != '-'
and average_pick != '-'
ORDER BY Cast(average_pick as float) ASC
