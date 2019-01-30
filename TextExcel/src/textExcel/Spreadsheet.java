package textExcel;

// Update this file with your own code.

public class Spreadsheet implements Grid
{
	Cell[][] cells;
	
	@Override
	public String processCommand(String command)
	{
		// TODO Auto-generated method stub
		String[] commands = command.split("\\s");
		for(String i : commands) {
			System.out.println(i);
			if(command.matches("[a-zA-Z]\\d+")) {
				SpreadsheetLocation cell = new SpreadsheetLocation(commands[0]);
				System.out.println("("+cell.row+", "+cell.col+")");
				return this.getCell(cell).fullCellText();
			}
			if((commands.length == 3) && commands[1] == "=") {
				SpreadsheetLocation cell = new SpreadsheetLocation(commands[0]);
				return this.getCell(cell).
			}
		}
		return "";
	}

	@Override
	public int getRows()
	{
		// TODO Auto-generated method stub
		return cells.length;
	}

	@Override
	public int getCols()
	{
		// TODO Auto-generated method stub
		return cells[0].length;
	}

	@Override
	public Cell getCell(Location loc)
	{
		// TODO Auto-generated method stub
		
		return cells[loc.getRow()][loc.getCol()];
	}

	@Override
	public String getGridText()
	{
		// TODO Auto-generated method stub
		return null;
	}
	
	public Spreadsheet() {
		cells = new Cell[20][12];
		for(int i = 0; i<20; i++) {
			for(int j = 0; j<12; j++) {
				cells[i][j] = new EmptyCell();
			}
		}
	}
	
	public Spreadsheet(int rows, int cols) {
		cells = new Cell[rows][cols];
		for(int i = 0; i<rows; i++) {
			for(int j = 0; j<cols; j++) {
				cells[i][j] = new EmptyCell();
			}
		}
	}

}
