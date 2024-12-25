import argparse
import core.globals

def parse_args():
    program = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=100))
    program.add_argument('-a', '--algo', help='select an algorithme [SAT,3SAT,SAT-2-3SAT]',dest='algorithm',default='SAT')
    program.add_argument('-f','--file', help='clauster input file',dest='clauster_file',default=None,type=str)
    program.add_argument('-n','--analyser', help='select an analyser [TIME,MEMORY]',dest='analyser',default='TIME')
    program.add_argument('-t', '--test', help='Generate N tests [will not read from file]',type=int,dest='test_number',default=0)
    program.add_argument('-g', '--graph', help='enable graph for analysing output; this is off per default [true,false]',type=bool,dest='graph',default=False)
    program.add_argument('-v', '--vars', help='Number of variables for random instance generation. Default=3', type=int, dest='nb_vars', default=3)
    program.add_argument('-c', '--clauses', help='Number of clauses for random instance generation. Default=3', type=int, dest='nb_clauses', default=3)
    program.add_argument('-mn', '--min', help='Min size of cluster. Default = 1', type=int, dest='clause_size_min', default=1)
    program.add_argument('-mx', '--max', help='Max size of cluster. Default = 3', type=int, dest='clause_size_max', default=3)
    
    args = program.parse_args()

    core.globals.algorithm = args.algorithm
    core.globals.analyser = args.analyser
    core.globals.clauster_file = args.clauster_file
    core.globals.graph = args.graph
    core.globals.test_number = args.test_number
    core.globals.nb_vars = args.nb_vars
    core.globals.nb_clauses = args.nb_clauses
    core.globals.clause_size_max = args.clause_size_max
    core.globals.clause_size_min = args.clause_size_min
    