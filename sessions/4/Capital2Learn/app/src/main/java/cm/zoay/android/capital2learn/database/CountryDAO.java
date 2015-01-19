package cm.zoay.android.capital2learn.database;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;

/**
 * Created by Zoay on 20/01/15.
 */
public class CountryDAO {

    private SQLiteDatabase db;
    private CountryHelper chelper;

    public CountryDAO(Context context)
    {
        chelper = new CountryHelper(context);
    }
}
