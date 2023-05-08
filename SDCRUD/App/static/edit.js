const convertFormat = () => {
    const inputs = document.querySelectorAll('.data-convert')
    inputs.forEach(item => {
        item.value = item.value.replace(',', '.')
    })
}

convertFormat()