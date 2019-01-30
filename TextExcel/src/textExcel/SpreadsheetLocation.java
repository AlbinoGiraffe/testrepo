package textExcel;

//Update this file with your own code.

public class SpreadsheetLocation implements Location
{
    String cell;
    int row;
    int col;
    
	@Override
    public int getRow()
    {
        // TODO Auto-generated method stub
		return row;
    }

    @Override
    public int getCol()
    {
        // TODO Auto-generated method stub
    	return col;
    }
    
    public SpreadsheetLocation(String cellName)
    {
        // TODO: Fill this out with your own code
    	cell = cellName;
    	this.row = Integer.parseInt(cell.substring(1))-1;
    	this.col = cell.charAt(0) - 'A';
    	
    }

}
