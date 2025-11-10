import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import LiveScores from './shared/components/Board.tsx'
import LiveLeaders from './shared/components/awayCard.tsx'

function App() {

  return (
    <>
      <LiveScores />
      <LiveLeaders />
    </>
  )
}

export default App
