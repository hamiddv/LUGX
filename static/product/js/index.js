const aboutProductHeadings = document.querySelectorAll(".js-about-product-headings")

aboutProductHeadings.forEach((element) => {
    element.addEventListener("click", (event) => {
        const headingData = event.target.getAttribute("data-heading")
        let aboutProductText = document.querySelector(`[data-heading-text='${headingData}']`)
        let activeProductText = document.getElementById("about-product__text-active")
        gsap.to(aboutProductText, {
            opacity: 1,
            display: "block",
            duration: 1.5
        })

        gsap.to(activeProductText, {
            opacity: 0,
            display: "none",
            duration: .000001
        })
    })
})