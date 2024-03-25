#include <stdio.h>

int main() {
    int king;
    int queen;
    int bishop;
    int knight;
    int rook;
    int pawn;
    scanf("%d %d %d %d %d %d", &king, &queen, &rook, &bishop, &knight, &pawn);
    
        
    int rking=1-king;
    int rqueen=1-queen;
    int rbishop=2-bishop;
    int rk=2-knight;
    int rrook=2-rook;
    int rpawn=8-pawn;
    
    printf("%d %d %d %d %d %d", rking, rqueen, rrook, rbishop, rk, rpawn);
}