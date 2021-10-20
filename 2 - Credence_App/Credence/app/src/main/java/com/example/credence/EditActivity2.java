package com.example.credence;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

public class EditActivity2 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit2);


        final EditText editText = findViewById(R.id.editedBelief);
        final EditText EditComment = findViewById(R.id.EditedComment);
        Button delete = findViewById(R.id.delete);
        Button save = findViewById(R.id.save);

        Intent intent = getIntent();

        String ID = intent.getStringExtra("ID");
        final int[] id = {Integer.parseInt(ID)};

        final SharedPreferences shrd = getSharedPreferences("demo", MODE_PRIVATE);
        String belief = shrd.getString("belief"+ id[0],"Belief");
        final String comment = shrd.getString("comment"+ id[0],"");
        final float per = shrd.getFloat("per"+ id[0],(float)25.55);
        final int total = shrd.getInt("id",1);

        editText.setText(belief);
        EditComment.setText(comment);

        ProgressBar progressBar = findViewById(R.id.progress_bar);
        TextView progressT = findViewById(R.id.progessText);

        progressBar.setProgress((int) per);
        progressT.setText(per+ " %");

        delete.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                while(id[0] <=(total-1) ){
                    String belief = shrd.getString("belief"+(id[0]+1),"");
                    float per = shrd.getFloat("per"+(id[0]+1),0f);
                    String comment = shrd.getString("comment"+(id[0]+1),"");

                    SharedPreferences.Editor editor = shrd.edit();
                    editor.putString("belief" + id[0],belief);
                    editor.putFloat("per" + id[0],per);
                    editor.putString("comment",comment);
                    editor.putInt("id",total-1);
                    editor.apply();
                    id[0] = id[0] +1;
                }

                Toast toast = Toast.makeText(EditActivity2.this, "Credence deleted" , Toast.LENGTH_SHORT);
                toast.show();
                Intent intent1 = new Intent(EditActivity2.this, MainActivity.class);
                startActivity(intent1);
            }
        });
        save.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                SharedPreferences.Editor editor = shrd.edit();
                editor.putString("belief"+id[0],editText.getText().toString());
                editor.putString("comment"+id[0],EditComment.getText().toString());
                editor.apply();
                Toast toast = Toast.makeText(EditActivity2.this, "Credence saved", Toast.LENGTH_SHORT);
                toast.show();
                Intent intent1 = new Intent(EditActivity2.this, MainActivity.class);
                startActivity(intent1);

            }
        });


    }
}