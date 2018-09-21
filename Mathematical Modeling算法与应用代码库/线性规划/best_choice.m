function [x, Q] = best_choice( s )
tempa = [0 0 0 0 0 s];
tempb = [-0.05 -0.27 -0.19 -0.185 -0.185 0];
f = tempa + (1-s)*tempb;
A = [diag([0, 0.025, 0.015, 0.055, 0.026]),-1*ones(5, 1)];
b = zeros(5,1);
Aeq = [1 1.01 1.02 1.045 1.65 0];
beq = 1;
[x, Q] = linprog(f, A, b, Aeq, beq, zeros(6, 1));
end

