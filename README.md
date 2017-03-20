# python_mipt_study_1-2
## ООО "Тупой скат"
Мы снова открылись! Ждем вас каждую среду с 12:00 до 16:00
###### Кто мы?
Мы - команда независимых разработчиков judge.mipt.ru, преследующие целью уничтожение сего сервиса.
###### Зачем?
~~**По фану**~~ Мы *помогаем* людям добиваться своего. Компилируемость вашего кода - **первая** проблема, о которой наша компания берет заботу.
###### Как мне поучаствовать в деле?
Все очень просто. Для начала откройте консольный гит-клиент на Вашей машине (ну, или чем вы там пользуетесь) и вставьте туда следующие команды:
``` 
git clone https://github.com/alekseik1/python_mipt_study_1-2 
```
Это все! Теперь вы - часть команды по борьбе с преступностью на верхних этажах КПМ!
###### Кто заказывает музыку в банкете?
Нас несколько, и мы стараемся держать друг друга в любви и согласии. Вот список тех, кто сделал этот проект возможным:
- [Klimkou](http://github.com/Klimkou)
- [alekseik1](http://github.com/alekseik1)
- [VS-Alex15](http://github.com/VS-Alex15)
- [Urnguk](http://github.com/Urnguk)
- [valshal](http://github.com/valshal)
- [iljun98](http://github.com/iljun98)

###### Я хочу помочь проекту, что мне делать?
Это очень просто! Просто откройте issue здесь, и ваши предложения будут рассмотрены. Форки, пулл реквесты и иже с ним будут с радостью рассмотрены нами)


N, M = map(int, input().split())
Edges = []
for i in range(M):
    start, end, weight = map(int, input().split())
    Edges.append([weight, start, end])
Edges.sort()
Comp = [i for i in range(N)]
tree = []
Ans = 0
for weight, start, end in Edges:
    if Comp[start] != Comp[end]:
        tree.append((start, end))
        Ans += weight
        a = Comp[start]
        b = Comp[end]
        for i in range(N):
            if Comp[i] == b:
                Comp[i] = a
