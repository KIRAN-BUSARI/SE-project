import React from 'react'

export default function Home() {
    return (
        <>
            {/* <p><b>This is Home</b></p> */}
            <div className="container mx-auto flex justify-center items-center h-[100vh] flex-col bg-slate-400">
                <div className="bg-slate-900 h-[50vh] flex justify-center items-center flex-col rounded-2xl">
                    <h1 className='text-3xl p-3 text-[#0095ff]'>Automated Student Attendence...👨🏻‍🎓</h1>
                    <button onClick={() => alert('Attendence is registerd')} className='p-3 text-[#ff7070]'>Present</button>
                    <button onClick={() => alert('Attendence is Not-Registerd')} className='p-3 text-[#ff7070]'>Absent</button>
                </div>
            </div>
        </>
    )
}
