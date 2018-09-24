function [] = show_res()
s = 0;
hold on;
while s <= 1
    [x, Q] = best_choice(s);
    Q = -Q;
    plot(s, Q, '*k');
    s = s + 0.001;
end

