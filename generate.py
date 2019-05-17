

def generate(password):
    output_list = []
    for i in range(10):
        output_list.append(password[:i] + '`' * (10 -i -1))
    return output_list

    
with open("prob.txt", 'a') as p:
    for i in generate("passwordwd"):
        p.write(i + "\n")


     













