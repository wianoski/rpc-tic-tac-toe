// These are all of the possible combinations
// that would win the game
var rows = [
    state.a0 + state.a1 + state.a2,
    state.b0 + state.b1 + state.b2,
    state.c0 + state.c1 + state.c2,
    state.a0 + state.b1 + state.c2,
    state.a2 + state.b1 + state.c0,
    state.a0 + state.b0 + state.c0,
    state.a1 + state.b1 + state.c1,
    state.a2 + state.b2 + state.c2
];
