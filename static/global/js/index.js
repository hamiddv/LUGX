let startFlag = true
let endFlag = true
window.addEventListener("scroll", () => {
    if (window.scrollY >= 92 && startFlag) {
        startFlag = false
        gsap.to("#main-header-container", {
            position: "fixed",
            top: "0",
            background: "#0071f8"
        })
        endFlag = true
    } else if (window.scrollY === 0 && endFlag) {
        endFlag = false
        gsap.to("#main-header-container", {
            position: "absolute",
            top: "20px",
            background: "transparent"
        })
        startFlag = true
    }
})
