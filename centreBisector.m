% m,c - parameters of line y = mx + c bisecting centre points
% (xCircle1,yCircle1), (xCircle2,yCircle2) - centres of 2 circles

function [m,c] = centreBisector(xCircle1,yCircle1,xCircle2,yCircle2)
    xmidpoint = (xCircle1 + xCircle2)/2;
    ymidpoint = (yCircle1 + yCircle2)/2;
    NOTm = (yCircle1 - yCircle2)/(xCircle1 - xCircle2);
    m = -1/NOTm;
    c = ymidpoint - m*xmidpoint;
end
