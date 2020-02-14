#!/bin/sh

# sort by part of speech
echo "Sorting"
sort -b -k 4 -k 3 tv_wlp.txt > tvs
echo "picking out words"
# awk '$3 !~ /^[0-9*@\/.-]/ &&  $3 ~ /[A-Za-z]+/ {print tolower($3), $4}' tvs | uniq > tmp
awk -f MATCH.awk tvs | uniq > words.wpos
egrep '#n' words.wpos | awk '{ print $1 }' | sort | uniq > words.nouns
grep '#vv' words.wpos | awk '{ print $1 }' | sort | uniq > words.verbs
grep '#aa' words.wpos | awk '{ print $1 }' | sort | uniq > words.adjectives
grep '#rr' words.wpos | awk '{ print $1 }' | sort | uniq> words.adjectives  # interrogative adverb
grep '#p' words.wpos | awk '{ print $1 }' | sort | uniq > words.pronouns
grep '#at' words.wpos | awk '{ print $1 }' | sort | uniq > words.articles
grep '#jj' words.wpos | awk '{ print $1 }' | sort | uniq > words.adverbs
grep '#cc' words.wpos | awk '{ print $1 }' | sort | uniq > words.conjunctions
grep '#cs' words.wpos | awk '{ print $1 }' | sort | uniq > words.conjunctions
grep '#ii' words.wpos | awk '{ print $1 }' | sort | uniq > words.prepositions

