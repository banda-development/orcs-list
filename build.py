N = 64

def main():
    with open("index.html", "r", encoding="utf-8") as index_file:
        data = index_file.read()
        for i in range(1, N):
            next_index = str(i+1)
            prev_index = str(i-1)
            if i == 1:
                prev_index = ""
            if i == N - 1:
                next_index = str(i)
            build_data = data.replace("data_0.csv", f"data_{i}.csv")
            build_data = build_data.replace("/orcs-list/index", f"/orcs-list/{prev_index}")
            build_data = build_data.replace("/orcs-list/1", f"/orcs-list/{next_index}")
            with open(f"{i}.html", "w", encoding="utf-8") as build_file:
                build_file.write(build_data)




if __name__ == "__main__":
    main()