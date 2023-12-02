import json
import os
VALID_SEARCH_KEYS = ['标题', '导演', '演员', '类型', '上映日期']


class MovieManagementSystem:

    def __init__(self, filename='movie_data.json'):
        self.filename = filename
        self.movies = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            return []

    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.movies, file, ensure_ascii=False, indent=2)

    def add_movie(self, movie):
        self.movies.append(movie)
        self.save_data()

    def delete_movie(self, movie_title):
        # 使用一个标志来检查是否删除了电影
        movie_deleted = False
        # 遍历电影列表
        for movie in self.movies:
            # 如果找到匹配的电影标题
            if movie['标题'] == movie_title:
                # 从列表中移除电影
                self.movies.remove(movie)
                movie_deleted = True
                # 停止迭代以删除仅第一个匹配的电影
                break
        # 仅当删除了电影时保存数据
        if movie_deleted:
            self.save_data()
            print("电影删除成功！")
        else:
            print("未找到匹配的电影。")

    def modify_movie(self, movie_title, new_info):
        # 使用一个标志来检查是否修改了电影
        movie_modified = False
        # 遍历电影列表
        for movie in self.movies:
            # 如果找到匹配的电影标题
            if movie['标题'] == movie_title:
                # 更新电影信息
                movie.update(new_info)
                movie_modified = True
                print("电影修改成功！")
        # 如果未找到匹配的电影
        if not movie_modified:
            print("未找到匹配的电影。")
        # 保存数据
        self.save_data()

    def search_movie(self, key, value):
        # 查找匹配的电影
        result = [movie for movie in self.movies if movie.get(key) == value]

        # 如果有匹配的电影
        if result:
            print("\n查询结果:")
            for movie in result:
                # 逐一打印电影信息
                print("\n电影信息:")
                print(f"标题: {movie.get('标题')}")
                print(f"导演: {movie.get('导演')}")
                print(f"演员: {', '.join(movie.get('演员', []))}")
                print(f"类型: {movie.get('类型')}")
                print(f"上映日期: {movie.get('上映日期')}")
        else:
            print("未找到匹配的电影。")

    def get_movie_count(self):
        return len(self.movies)

    def display_all_movies(self):
        if not self.movies:
            print("当前没有电影数据。")
        else:
            print("\n所有电影:")
            for movie in self.movies:
                print("\n电影信息:")
                print(f"标题: {movie.get('标题')}")
                print(f"导演: {movie.get('导演')}")
                print(f"演员: {', '.join(movie.get('演员', []))}")
                print(f"类型: {movie.get('类型')}")
                print(f"上映日期: {movie.get('上映日期')}")


if __name__ == "__main__":
    movie_system = MovieManagementSystem()

    while True:
        print("\n电影管理系统")
        print("1. 添加电影")
        print("2. 删除电影")
        print("3. 修改电影")
        print("4. 查询电影")
        print("5. 统计电影数量")
        print("6. 显示所有电影")
        print("7. 退出")

        choice = input("请输入您的选择 (1-7): ")

        if choice == '1':
            title = input("请输入电影标题: ")
            director = input("请输入导演: ")
            actors = input("请输入演员(以逗号分隔）: ").split(',')
            genre = input("请输入电影类型: ")
            release_date = input("请输入上映日期: ")

            movie_info = {
                '标题': title,
                '导演': director,
                '演员': actors,
                '类型': genre,
                '上映日期': release_date
            }

            movie_system.add_movie(movie_info)
            print("电影添加成功！")
            input("按任意键继续...")  # 等待用户按下任意键

        elif choice == '2':
            title_to_delete = input("请输入要删除的电影标题: ")
            movie_system.delete_movie(title_to_delete)
            input("按任意键继续...")  # 等待用户按下任意键

        elif choice == '3':
            title_to_modify = input("请输入要修改的电影标题: ")
            new_director = input("请输入新导演: ")
            new_actors = input("请输入新演员 (逗号分隔): ").split(',')
            new_genre = input("请输入新类型: ")
            new_release_date = input("请输入新上映日期: ")

            new_info = {
                '导演': new_director,
                '演员': new_actors,
                '类型': new_genre,
                '上映日期': new_release_date
            }

            movie_system.modify_movie(title_to_modify, new_info)
            print("电影修改成功！")
            input("按任意键继续...")  # 等待用户按下任意键

        elif choice == '4':
            search_key = input("请输入查询关键字 (例如，标题、导演、演员、类型): ")
            if search_key not in VALID_SEARCH_KEYS:
                print("无效的查询关键字。请使用有效的关键字，如标题、导演、演员、类型、上映日期。")
            else:
                search_value = input(f"请输入要查询的{search_key}: ")
                movie_system.search_movie(search_key, search_value)
            input("按任意键继续...")  # 等待用户按下任意键

        elif choice == '5':
            movie_count = movie_system.get_movie_count()
            print(f"当前电影数量: {movie_count}")
            input("按任意键继续...")  # 等待用户按下任意键

        elif choice == '6':
            movie_system.display_all_movies()
            input("按任意键继续...")  # 等待用户按下任意键

        elif choice == '7':
            print("退出电影管理系统。再见！")
            break

        else:
            print("无效的选择。请输入1到7之间的数字。")
