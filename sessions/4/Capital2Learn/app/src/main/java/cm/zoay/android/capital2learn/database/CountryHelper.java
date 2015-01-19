package cm.zoay.android.capital2learn.database;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.util.Log;

import java.sql.SQLException;

import cm.zoay.android.capital2learn.utils.Utils;

/**
 * Created by Zoay on 19/01/15.
 */

public class CountryHelper extends SQLiteOpenHelper{

    private static final String DATABASE_NAME = "capital_of_world.db";
    private static final String TABLE_NAME = "africa_country";

    private static final String UID = "_id";
    private static final String COUNTRY = "country";
    private static final String DIMINUTIF = "diminutif";
    private static final String CAPITAL = "capital";

    private static final int DATABASE_VERSION = 1;

    private static final String CREATE_TABLE = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME + "( " +
               UID + " INT PRIMARY KEY autoincrement NOT NULL," +
               COUNTRY + " TEXT NOT NULL, " +
               DIMINUTIF + " TEXT NOT NULL," +
               CAPITAL + " TEXT NOT NULL" +
            ")";

    private static final String DROP_TABLE = "DROP TABLE IF EXISTS " + TABLE_NAME;

    private Context context;

    public CountryHelper(Context context)
    {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
        this.context = context;
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(CREATE_TABLE);
        Utils.message(context, "onCreate called --> the database has been created");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL(DROP_TABLE);
        onCreate(db);
        Utils.message(context, "onUpgrade called!");
    }

    public static final String getUid()
    {
        return UID;
    }

    public static final String getCountry()
    {
        return COUNTRY;
    }

    public static final String getDiminutif()
    {
        return DIMINUTIF;
    }

    public static final String getCapital()
    {
        return CAPITAL;
    }
}
