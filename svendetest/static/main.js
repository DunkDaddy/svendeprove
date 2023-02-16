async function getPoints() {
    let response = await fetch('http://10.130.54.25:8000/data/personlsite/', {
        method: 'get',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
            'Authorization': 'Token 10221976ae7eebb749b62cb74de527cd6500697a'
        }
    })

    let data = await response.json()
    console.log(await data)
}


async function getStats() {
    let response = await fetch('http://10.130.54.25:8000/data/personlsite/', {
        method: 'get',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
            'Authorization': 'Token 10221976ae7eebb749b62cb74de527cd6500697a'
        }
    })

    let data = await response.json()
    console.log(await data)
}