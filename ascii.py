def canvas():
    pound_sign = '#'*(10)
    blank_line = "#"+(' '*(8))+'#'
    # grid_line = "#"+(' '*N)+('*'*N)+(' '*N)+"#"
    print('{}{}{}'.format(pound_sign+'\n',\
                    (blank_line+'\n')*8,\
                    # (grid_line+'\n')*N,\
                    # (blank_line+'\n')*int(N/2),\
                    pound_sign))