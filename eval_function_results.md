Maze                    Depth   Score
testAdversarial         12      257
smallAdversarial        2       92
aiAdversarial           10      86
anuAdversarial          8       -109
mazeAdversarial         10      -20
smallDenseAdversarial   6       253
aiDenseAdversarial      6       -267
anuDenseAdversarial     6       207
mazeDenseAdversarial    6       9


python red_bird.py -p MinimaxAgent -l adv_search_layouts/testAdversarial.lay -a depth=12 -b GreedyBlackBirdAgent --timeout 60 -c -q
python red_bird.py -p MinimaxAgent -l adv_search_layouts/anuAdversarial.lay -a depth=8 -b GreedyBlackBirdAgent --timeout 60 -c -q
python red_bird.py -p MinimaxAgent -l adv_search_layouts/mazeAdversarial.lay -a depth=10 -b GreedyBlackBirdAgent --timeout 60 -c -q
python red_bird.py -p MinimaxAgent -l adv_search_layouts/smallDenseAdversarial.lay -a depth=6 -b GreedyBlackBirdAgent --timeout 60 -c -q
python red_bird.py -p MinimaxAgent -l adv_search_layouts/aiDenseAdversarial.lay -a depth=6 -b GreedyBlackBirdAgent --timeout 60 -c -q
python red_bird.py -p MinimaxAgent -l adv_search_layouts/anuDenseAdversarial.lay -a depth=6 -b GreedyBlackBirdAgent --timeout 60 -c -q
python red_bird.py -p MinimaxAgent -l adv_search_layouts/mazeDenseAdversarial.lay -a depth=10 -b GreedyBlackBirdAgent --timeout 60 -c -q

