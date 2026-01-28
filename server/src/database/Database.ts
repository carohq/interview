import * as fs from 'fs'
import * as path from 'path'

export type HeadcountStatus = 'in_seat' | 'pending_term' | 'pending_start'

export interface Headcount {
  id: string
  name: string
  status: HeadcountStatus
  costCenterId: string
}

export interface CostCenter {
  id: string
  name: string
  parentId: string | null
}

export class Database {
  private headcountData: Headcount[]
  private costCentersData: CostCenter[]

  constructor() {
    this.headcountData = this.loadJSON<Headcount>('data/headcount.json')
    this.costCentersData = this.loadJSON<CostCenter>('data/cost-centers.json')
  }

  private loadJSON<T>(filename: string): T[] {
    const filePath = path.join(__dirname, filename)
    const fileContent = fs.readFileSync(filePath, 'utf-8')
    return JSON.parse(fileContent) as T[]
  }

  /**
   * Get all headcount records
   */
  getHeadcount(): Headcount[] {
    return this.headcountData
  }

  /**
   * Get a specific headcount record by ID
   */
  getHeadcountById(id: string): Headcount | undefined {
    return this.headcountData.find(hc => hc.id === id)
  }

  /**
   * Get all cost centers
   */
  getCostCenters(): CostCenter[] {
    return this.costCentersData
  }

  /**
   * Get a specific cost center by ID
   */
  getCostCenterById(id: string): CostCenter | undefined {
    return this.costCentersData.find(cc => cc.id === id)
  }
}
