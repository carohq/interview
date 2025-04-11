import express, { Request, Response } from 'express'

const app = express()
const PORT = process.env.PORT || 3000

app.get('/api/hello', (req: Request, res: Response) => {
  res.json({ message: 'Hello from Expressses + TypeScript!' })
})

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`)
})