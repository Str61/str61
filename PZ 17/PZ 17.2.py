import tkinter as tk
import random


def main():
    # Создаем главное окно
    root = tk.Tk()
    root.title("Простая работа с матрицами")
    root.geometry("500x400")

    # Функция для обработки матрицы
    def process_matrix():
        try:
            # Получаем размеры матрицы
            rows = int(entry_rows.get())
            cols = int(entry_cols.get())

            # Создаем случайную матрицу
            matrix = []
            for _ in range(rows):
                row = [random.randint(-10, 10) for _ in range(cols)]
                matrix.append(row)

            # Обрабатываем матрицу (возводим отрицательные в квадрат)
            result = []
            for row in matrix:
                new_row = [x ** 2 if x < 0 else x for x in row]
                result.append(new_row)

            # Показываем результаты
            text_original.delete(1.0, tk.END)
            text_result.delete(1.0, tk.END)

            text_original.insert(tk.END, "Исходная матрица:\n")
            for row in matrix:
                text_original.insert(tk.END, f"{row}\n")

            text_result.insert(tk.END, "Результат:\n")
            for row in result:
                text_result.insert(tk.END, f"{row}\n")

        except:
            tk.messagebox.showerror("Ошибка", "Проверьте введенные данные")

    # Элементы интерфейса
    frame_input = tk.Frame(root)
    frame_input.pack(pady=10)

    tk.Label(frame_input, text="Строки:").pack(side=tk.LEFT)
    entry_rows = tk.Entry(frame_input, width=5)
    entry_rows.pack(side=tk.LEFT, padx=5)

    tk.Label(frame_input, text="Столбцы:").pack(side=tk.LEFT)
    entry_cols = tk.Entry(frame_input, width=5)
    entry_cols.pack(side=tk.LEFT, padx=5)

    btn_process = tk.Button(root, text="Обработать матрицу", command=process_matrix)
    btn_process.pack(pady=5)

    frame_text = tk.Frame(root)
    frame_text.pack(fill=tk.BOTH, expand=True)

    text_original = tk.Text(frame_text, height=8, width=30)
    text_original.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    text_result = tk.Text(frame_text, height=8, width=30)
    text_result.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()