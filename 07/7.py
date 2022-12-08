
fs = {}

def totalDir(dir):
    print(fs.keys())
    print(fs[dir])
    
    subdir_size = 0
    for subdir in fs[dir]['subdirs']:
        totalDir(subdir)
        subdir_size += fs[subdir]['total_size']
    fs[dir]['total_size'] = fs[dir]['this_size'] + subdir_size

with open('input.txt') as input:
    output = []
    while line := input.readline().strip():
        if line.startswith('$'):
            output.append([line,[]])
        else:
            output[-1][1].append(line)

    cwd = []
 
    for command in output:
        match command[0][2:4]:
            case 'cd':
                match command[0][5:]:
                    case '..':
                        cwd.pop()
                    case _:
                        cwd.append(command[0][5:])
            case 'ls':
                for data in command[1]:
                    if data.startswith('dir'):
                        try:
                            fs['/'.join(cwd)]['subdirs'].append('/'.join(cwd + list(data[4:])))
                        except KeyError:
                            fs['/'.join(cwd)] = { 'total_size': 0, 'this_size': 0, 'subdirs': ['/'.join(cwd + list(data[4:]))]}
                    else:
                        size = int(data.split()[0])
                        try:
                            fs['/'.join(cwd)]['this_size'] += size
                        except KeyError:
                            fs['/'.join(cwd)] = { 'total_size': 0, 'this_size': size, 'subdirs': []}  
   
    totalDir(list(fs.keys())[0])
    
    sum_of_10k = 0
    for dir in fs.keys():
        if fs[dir]['total_size'] <= 100000:
            sum_of_10k += fs[dir]['total_size']
    print(f"sum of directories up to 10k: {sum_of_10k}")
