const cells = document.querySelectorAll(".cell");

cells.forEach((cell) => {
    cell.addEventListener("focus", (e) => {
        const previousActiveCell = document.querySelector(".active-cell");
        if (previousActiveCell) {
            previousActiveCell.classList.remove("active-cell");
        }
        const cellId = e.target.id;
        const activeCell = document.getElementById(cellId);
        activeCell.classList.add("active-cell");
    });
});
