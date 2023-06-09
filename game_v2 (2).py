def score_game(optimal_predict) -> int:
  import numpy as np
  """ За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        optimal_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
  count_ls = []
  np.random.seed(1)  # фиксируем сид для воспроизводимости
  random_array = np.random.randint(1, 101, size=(1000))  # загадали список онлайн переводчик чисел

  for number in random_array:
    count_ls.append(optimal_predict(number))

  score = int(np.mean(count_ls))
  print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
score_game(optimal_predict)