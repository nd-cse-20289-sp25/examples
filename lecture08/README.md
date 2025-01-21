# Examples 08

# Pipeline: Powerful Pattern

Three volunteers to role-play and demonstrate a pipeline.

1. How many Starbursts are pink?

        read | filter pink | count

2. How many different colors of Starbursts do we have?

        read | sort | uniq

# Pipeline: Demonstration

1. How many instances of bash are running?

        $ ps aux | grep bash | grep -v grep | wc -l

2. How many different types of shells are being used?

        $ ps aux | grep -Ev '(grep|ssh|flush)' | grep -Eo '(bash|zsh)' | sort | uniq

    To see how many of each, do `uniq -c`

3. Who has the most processes?

        for user in $(ps aux | cut -d ' ' -f 1 | sort | uniq); do
            echo $(ps aux | grep -v grep | grep ^$user | wc -l) $user
        done | sort -rn

    Alternatively:

        ps aux | cut -d ' ' -f 1 | sort | uniq -c | sort -rn

4. Who has the most TROLL/sleep processes?

        ps aux | grep TROLL | cut -d ' ' -f 1 | sort | uniq -c | sort -rn

# Regular Expressions: Syntax

        $ echo "Mayleen" | grep -E '.*'             # Match all letters

        $ echo "Mayleen" | grep -E 'e*'             # Match zero or more e's

        $ echo "Mayleen" | grep -E 'a?'             # Match zero or one a's

        $ echo "Mayleen" | grep -E 'e{2}'           # Match exactly 2 e's

        $ echo "Daniel" | grep -E '[aei]*'          # Match any a, e, i's

        $ echo "Daniel" | grep -E '[aei]+'	    # Match one or more of a, e, i

        $ echo "Daniel" | grep -E '[^aei]+'         # Match everything but a, e, i

        $ echo "Daniel" | grep -E '^D'              # Match start

        $ echo "Daniel" | grep -E 'l$'              # Match end

        $ echo "Danielle" | grep -E '(e).*\1'      # Match with group references

# Regular Expressions: Examples

1. All the strings                                      .*

2. Only charmander and chespin                          ^[ch]

3. All words with two t's                               t{2}

4. Words that don't start with a vowel                  ^[^aeiou]

5. All words with two consecutive vowels                [aeiou]{2}

6. All words with two consecutive letters (same)        (.)\1

7. All words that begin and end with the same letter    ^(.).*\1$

8. All words with exactly 2 of r, s, or t               '^[^rst]*[rst][^rst]*[rst][^rst]*$'

# Activity: Contact Harvesting

1. Extract all the phone numbers

        $ curl -sLk https://yld.me/d51B | grep -Eo '[0-9]{3}-[0-9]{3}-[0-9]{4}' | sort | uniq

2. Extract all the email addresses

        $ curl -sLk https://yld.me/d51B | grep -Eo '>[[:alnum:]]+@[[:alnum:]\.]+' | cut -b 2- | sort | uniq

3. Extract all the "Assistant" positions

        $ curl -sLk https://yld.me/d51B | grep -Eo '>[^>]*+Assistant[^<]*' | cut -b 2- | sort

# Activity: CSE Curriculum

1. How many MATH vs PHYS vs CSE courses?

        $ curl -sLk https://yld.me/zlH
                | grep -v meta
                | grep credits
                | grep -Eo '(MATH|PHYS|CSE)'
                | sort
                | uniq -c

2. How many credits per semester?

        $ curl -sLk https://yld.me/zlH
                | grep -v meta
                | grep -Eo 'Total Credit Hours: [0-9\.]+'
                | cut -d ' ' -f 4
                | sort
                | uniq -c

        $ curl -sLk https://yld.me/zlH
                | grep -v meta
                | sed -En 's/.*Total Credit Hours: ([0-9\.]+).*/\1/p'
                | sort
                | uniq -c

3. How many sophomore CSE courses?

        $ curl -sLk https://yld.me/zlH
                | grep -Eo 'CSE 2[0-9]{4}'
                | sort

        $ curl -sLk https://yld.me/zlH
                | sed 's/<br>/\n/g'
                | sed -En 's/.*(CSE 2[0-9]{4}).*/\1/p'
                | sort

4. How many sophomore CSE credits?

        $ curl -sLk https://yld.me/zlH
                | sed 's/<br>/\n/g' 
                | sed -En 's/.*(CSE 2[0-9]{4}).*([0-9]) credits.*/\2/p'
                | awk '{ sum += $1 } END { print sum }'

5. How many different types of electives?

        $ curl -sLk https://yld.me/zlH
                | grep -v meta
                | sed -E 's/<(br|p)>/\n/g' 
                | sed -En 's/([^>]+ Elective).*credits.*/\1/p' 
                | sort
                | uniq -c
