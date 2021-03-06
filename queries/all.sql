'SELECT pos,fname, lname, pos_type, Cast(average_pick as float), Cast(percent_drafted as float), Cast(o_rank as int), Cast(psr_rank as int), Cast(season_stats->>\'1\' as float) as season_g, Cast(season_stats->>\'2\' as float) as season_a, Cast(season_stats->>\' 4\' as float) as seasom_plus_minus, Cast(season_stats->>\'8\' as float) as season_ppp, Cast(season_stats->>\'14\' as float) as season_sog , Cast(season_stats->>\'31\' as float) as season_hits, Cast(season_stats->>\'19\' as float) as season_w, Cast(season_stats->>\'22\' as float) as season_ga, Cast(season_stats->>\'23\' as float) as season_gaa, Cast(season_stats->>\'24\' as float) as season_shots_against, Cast (season_stats->>\'25\' as float) as season_saves, Cast(season_stats->>\'26\' as float) as season_sp, Cast(season_stats->>\'27\' as float) as season_so, Cast(projected_stats->>\'1\' as float) as projected_g, Cast(projected_stats->>\'2\' as float) as projected_a, Cast(projected_stats->>\'4\' as float) as projected_plus_minus, Cast(projected_stats->>\'8\' as float) as projected_ppp, Cast(projected_stats->>\'14\' as float) as projected_sog, Cast(projected_stats->>\'31\' as float) as projected_hits, Cast(projected_stats->>\'19\' as float) as projected_w, Cast(projected_stats->>\'22\' as float) as projected_ga, Cast(projected_stats->>\'23\' as float) as projected_gaa, Cast(projected_stats->>\'24\' as float) as projected_shots_against, Cast(projected_stats->>\'25\' as float) as projected_saves, Cast(projected_stats->> \'26\' as float) as projected_sp, Cast(projected_stats->>\'27\' as float) as projected_so FROM nhl.players where average_round != \'-\' and Cast(season_stats->>\'1\' as text) != Cast(\'-\' as text) and average_pick != \'-\' ORDER BY Cast(average_pick as float) ASC'

SELECT pos,pos_type, fname, lname, Cast(average_pick as float),
Cast(percent_drafted as float),
Cast(o_rank as int),
Cast(psr_rank as int),
Cast(season_stats->>'1' as float) as season_g,
Cast(season_stats->>'2' as float) as season_a,
Cast(season_stats->>'4' as float) as seasom_plus_minus,
Cast(season_stats->>'8' as float) as season_ppp,
Cast(season_stats->>'14' as float) as season_sog,
Cast(season_stats->>'31' as float) as season_hits,
Cast(season_stats->>'19' as float) as season_w,
Cast(season_stats->>'22' as float) as season_ga,
Cast(season_stats->>'23' as float) as season_gaa,
Cast(season_stats->>'24' as float) as season_shots_against,
Cast(season_stats->>'25' as float) as season_saves,
Cast(season_stats->>'26' as float) as season_sp,
Cast(season_stats->>'27' as float) as season_so,
Cast(projected_stats->>'1' as float) as projected_g,
Cast(projected_stats->>'2' as float) as projected_a,
Cast(projected_stats->>'4' as float) as projected_plus_minus,
Cast(projected_stats->>'8' as float) as projected_ppp,
Cast(projected_stats->>'14' as float) as projected_sog,
Cast(projected_stats->>'31' as float) as projected_hits,
Cast(projected_stats->>'19' as float) as projected_w,
Cast(projected_stats->>'22' as float) as projected_ga,
Cast(projected_stats->>'23' as float) as projected_gaa,
Cast(projected_stats->>'24' as float) as projected_shots_against,
Cast(projected_stats->>'25' as float) as projected_saves,
Cast(projected_stats->>'26' as float) as projected_sp,
Cast(projected_stats->>'27' as float) as projected_so
FROM nhl.players
where average_round != '0'
and average_pick != '0'
ORDER BY Cast(average_pick as float) ASC

