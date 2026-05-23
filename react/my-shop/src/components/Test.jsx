import { useEffect, useState } from "react"

function Counter(){
    const [count, setCount] = useState(0)
    useEffect(()=>{

        setTimeout(()=>{
            console.log("Hello")
        }, 3000)
    }, [])

    const handleClick = ()=>{
        setCount(p=>p+1)
    }
    return(
        <div>
            <h1>{count}</h1>
            <button onClick={handleClick}>+</button>
        </div>
    )
}

export default Counter