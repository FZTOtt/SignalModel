# Моделирование отражения сигнала, излучаемого антенной, от цели

## Идея
Стоит задача промоделировать работу приемной и передающей антенн. Сигнал от передающей антенны подаётся на цель, а отражение этого сигнала принимается при помощи приёмной антенны. Предполагается разработка ПО, реализованного на языке C++ (в лучшем случае) или Python. 
ПО должно поддерживать:
1. Задание координат и диаграмы направленности антенны.
2. Задание координат и положения цели (у модели цели своя система координат, которую предполагается вращать для поворота цели).
3. Чтение модели цели из внешнего файла (формат, поддерживаемый САПР: .step).
4. Покрытие поверхности модели различными сетками.
5. Моделирование облучения цели сигналом и его приёма одной антенной (моностатический случай).
6. Моделирование облучения цели сигналом передающей катушки и обработка сигнала приёмной катушкой (бистатический случай).

## План.
1. Изучение теоретического материала. Математические выкладки и формулы по отражению и приёму сигнала.
2. Разделение моделирования на дальнюю зону и ближнюю. То есть разработка двух решателей: упрощённого и более точного.
