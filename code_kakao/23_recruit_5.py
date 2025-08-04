def solution(commands):
    MAX_ROW, MAX_COL = 50, 50
    cell_value = [None] * (MAX_ROW * MAX_COL)           # Value of each cell
    cell_head = list(range(0, MAX_ROW * MAX_COL))       # Head cell index for each cell

    answer = []
    for c in commands:
        c_list = c.split(' ')
        # Command type 1
        if c_list[0] == "UPDATE" and len(c_list) == 4:
            r, c = int(c_list[1]) - 1, int(c_list[2]) - 1
            cell_id = r * MAX_COL + c
            cell_value[cell_head[cell_id]] = c_list[3]      # Update the "value" only for the "head"

        # Command type 2
        elif c_list[0] == "UPDATE":
            for i in range(MAX_ROW * MAX_COL):
                if cell_value[cell_head[i]] == c_list[1]:
                    cell_value[cell_head[i]] = c_list[2]

        # Command type 3
        elif c_list[0] == "MERGE":
            r1, c1, r2, c2 = int(c_list[1]) - 1, int(c_list[2]) - 1, int(c_list[3]) - 1, int(c_list[4]) - 1
            cell_id_1, cell_id_2 = r1 * MAX_COL + c1, r2 * MAX_COL + c2
            if cell_id_1 == cell_id_2:
                continue
            head_id_1, head_id_2 = cell_head[cell_id_1], cell_head[cell_id_2]
            value = cell_value[head_id_1] if cell_value[head_id_1] is not None else cell_value[head_id_2]

            # Update value of the head for group 1
            cell_value[head_id_1] = value

            # For group 2, update "head"
            for i in range(MAX_ROW * MAX_COL):
                if cell_head[i] == head_id_2:
                    cell_head[i] = head_id_1

        # Command type 4
        elif c_list[0] == "UNMERGE":
            r, c = int(c_list[1]) - 1, int(c_list[2]) - 1
            cell_id = r * MAX_COL + c
            head_id = cell_head[cell_id]
            value = cell_value[head_id]

            for i in range(MAX_ROW * MAX_COL):
                if cell_head[i] == head_id:
                    if (i == cell_id):
                        cell_value[i] = value
                    else:
                        cell_value[i] = None
                    cell_head[i] = i        # Clear its "head_id" as its own id

        # Command type 5
        elif c_list[0] == "PRINT":
            r, c = int(c_list[1]) - 1, int(c_list[2]) - 1
            cell_id = r * MAX_COL + c
            if cell_value[cell_head[cell_id]] is not None:      # Access "head id"
                answer.append(cell_value[cell_head[cell_id]])
            else:
                answer.append("EMPTY")
    return answer


if __name__ == '__main__':
    commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", 
                "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", 
                "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", 
                "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]

    ans = solution(commands)
    print(ans)