package textExcel;

// Update this file with your own code.

public class Spreadsheet implements Grid
{
	Cell[][] cell;
	
	@Override
	public String processCommand(String command)
	{
		// TODO Auto-generated method stub
		return "";
	}

	@Override
	public int getRows()
	{
		// TODO Auto-generated method stub
		return cell.length;
	}

	@Override
	public int getCols()
	{
		// TODO Auto-generated method stub
		return cell[0].length;
	}

	@Override
	public Cell getCell(Location loc)
	{
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public String getGridText()
	{
		// TODO Auto-generated method stub
		return null;
	}
	
	public Spreadsheet() {
		cell = new Cell[20][12];
		for(int i = 0; i<20; i++) {
			for(int j = 0; j<12; j++) {
				cell[i][j] = new EmptyCell();
			}
		}
	}

}
