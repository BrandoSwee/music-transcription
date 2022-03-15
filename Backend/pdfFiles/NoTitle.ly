% #(set-global-staff-size 14)

    \header {
        composer = \markup { Me }
        subtitle = \markup { You }
     title = \markup {No Title}
    }
    \layout {
        indent = 0
    }


% \context Score = "Score"
<<
    \context PianoStaff = "Piano_Staff"
    <<
        \context Staff = "R_Staff"
        {
            \context Voice = "R_Voice"
            {
                <c'' dis''>4
                <c'' d'' dis''>4
                <gis''>4
                <gis' c'' gis''>4
                <gis' c'' d'' gis''>4
                <gis' c'' dis'' f''>4
                <g''>4
                <c'' d'' g''>4
                <c''>4
                <gis' c''>4
                <dis' ais' c'' g''>4
                r4
                <d' d'' f''>4
                r4
                <d' b' cis'' d''>4
                <b' d''>4
                <c' g' c'' dis''>4
                <c'' d'' dis''>4
                <gis''>4
                <c' c''>4
                <d''>4
                <b' dis'' f''>4
                <g''>4
                <c'' d'' g''>4
                <c''>4
                <dis' gis' ais' c'' gis''>4
                <dis' ais' c'' g''>4
                r4
                <d' ais' d'' f''>4
                r4
                <d' b' cis'' d''>4
                <d' g' g''>4
                <g''>4
                <ais' c'' d''>4
                <c' ais' c'' g''>4
                <ais' c'' d'' f'' g'' gis''>4
                <d' b' c'' f'' g''>4
                <d' b' d''>4
                <b' d'' g''>4
                <d' b' d'' f'' g'' gis''>4
                <d' a' d'' f'' g''>4
                <b' d'' fis'' g''>4
                <d' a' d'' g''>4
                <d' d'' g'' d'''>4
                <f'' fis''>4
                <dis' ais' dis''>4
                <dis' c'' dis''>4
                <dis' c''>4
                <gis''>4
                <d' d''>4
                <d' b' d'' d'''>4
                <d' d''>4
                <d' c'' d'' g''>4
                <dis' g''>4
                <c''>4
                <dis' c''>4
                <dis' f' c'' f''>4
                <f' gis' c'' f'' gis''>4
                <f' c''>4
                <gis' b' dis''>4
                <d' b' d''>4
                <dis' ais'>4
                <d' d''>4
                <d' f' c'' d''>4
                <c'' d'' dis''>4
                <c'' d''>4
                <gis''>4
                <c' c''>4
                <gis' c'' d'' gis''>4
                <gis' c'' dis'' f''>4
                <g''>4
                <c'' d'' g''>4
                <c''>4
                <gis' ais' c'' gis''>4
                <dis' ais' c'' g''>4
                r4
                <d' ais' d'' f''>4
                <d' f' c'' f''>4
                <d' b' d''>4
                <c'>4
                <g' c'' dis''>4
                <c'' d''>4
                <gis''>4
                <c' c''>4
                <d''>4
                <b' dis'' f''>4
                <g''>4
                <c'' d'' g''>4
                <c''>4
                <dis' gis' ais' c'' gis''>4
                <dis' ais' c'' g''>4
                <f''>4
                <d' ais' d'' f''>4
                <d' f' c'' d'' f''>4
                <d' b' d''>4
                <d' g' d'' g''>4
                <g''>4
                <dis' ais' d''>4
                <c'' g''>4
                <dis' ais' d'' g'' gis''>4
                <b' c'' f'' g''>4
                <d' d''>4
                <b' d'' g''>4
                <d' b' d'' g'' gis''>4
                <d' d'' f'' g''>4
                <b' d'' fis'' g''>4
                <d' d''>4
                <d' d'' g'' d'''>4
                <f'' fis'' g''>4
                <dis' ais' dis''>4
                <c'' dis''>4
                <dis' c'' dis''>4
                <gis''>4
                <d' d''>4
                <d' b' d'' d'''>4
                <d' d''>4
                <d' c'' d'' g''>4
                <dis' d'' g''>4
                <c''>4
                <c''>4
                <dis' c'' f''>4
                r2
                <f' gis' c'' dis'' gis''>4
                <d' b' d''>4
                <dis' ais'>4
                <d' d''>4
                <d' f' c'' d''>4
            }
        }
        \context Staff = "LH_Staff"
        {
            \context Voice = "LH_Voice"
            {
                \clef "bass"
                <c g>4
                r4
                <c gis>4
                <gis>4
                <c gis>4
                <gis>4
                <c>4
                r4
                <gis>4
                <gis>4
                <gis>4
                <ais>4
                <g, g>4
                <f>4
                <b>4
                <b>4
                <c>4
                <g g>4
                <c gis>4
                r4
                <b, b>4
                <b>4
                <c>4
                <g>4
                <gis>4
                <gis>4
                <gis>4
                <ais>4
                <g, g>4
                <f>4
                <b>4
                r4
                <c>4
                <g>4
                <c>4
                <g>4
                <b, b>4
                <g>4
                <g b>4
                r4
                <d>4
                <b>4
                <d g>4
                <g>4
                <g,>4
                <dis>4
                r2
                <b,>4
                <g>4
                <b, b>4
                <g>4
                <c>4
                r4
                <c>4
                r4
                <c>4
                <gis>4
                <c>4
                <gis>4
                <g, g>4
                <c dis>4
                <g,>4
                r4
                <c g>4
                r4
                <c gis>4
                <gis>4
                <c gis>4
                <gis>4
                <c gis>4
                <g>4
                <gis>4
                <gis>4
                <gis>4
                <ais>4
                <g, g>4
                r4
                <b>4
                <b>4
                <c>4
                <g g>4
                <c>4
                <gis>4
                <b, b>4
                <b>4
                <c>4
                <g>4
                <gis>4
                <gis>4
                <gis>4
                <ais>4
                <g, g>4
                r4
                <b>4
                r4
                <c>4
                <g>4
                <c c>4
                <g>4
                <b, b>4
                <g>4
                <g b>4
                r4
                <d>4
                <b>4
                <d g>4
                <g>4
                <g, g>4
                <c dis>4
                r2
                <b,>4
                <g>4
                <b, d b>4
                <g>4
                <c>4
                r4
                <c>4
                r4
                <c>4
                <f>4
                <f>4
                <gis>4
                <g, g b>4
                <c dis>4
                <g, c>4
                r4
            }
        }
    >>
>>
%! abjad.LilyPondFile._get_format_pieces()
\version "2.22.1"
%! abjad.LilyPondFile._get_format_pieces()
\language "english"