f2 = open(('/home/duguodong/datasets/Replay_Attack/crop/devel/develList.txt'), 'w')

path = '/home/duguodong/datasets/Replay_Attack/crop/devel'

f1 = open((path + '/real/devel_real.txt'), 'r')
line = f1.readline()
line = line[:-1]       #remove lastest change line symbol
#  print line
idx = 0
while line:
    idx += 1
#    print idx
    f2.write(path + '/real/' + line + ' ' + '0\n')
#    img = io.imread(path + line)

    line = f1.readline()
    line = line[:-1]
#    print line
f1.close

f3 = open((path + '/attack/hand/devel_attack_hand.txt'), 'r')
line = f3.readline()
line = line[:-1]
idx = 0
while line:
    idx += 1
    f2.write(path + '/attack/hand/' + line + ' ' + '1\n')
    line = f3.readline()
    line = line[:-1]
f3.close

f4 = open((path + '/attack/fixed/devel_attack_fixed.txt'), 'r')
line = f4.readline()
line = line[:-1]
idx = 0
while line:
    idx += 1
    f2.write(path + '/attack/fixed/' + line + ' ' + '1\n')
    line = f4.readline()
    line = line[:-1]
f4.close

f2.close
